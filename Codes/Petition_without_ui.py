import json
import datetime
import nltk
import boto3
import pdfplumber
import os
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

AWS_ACCESS_KEY_ID = ''   
AWS_SECRET_ACCESS_KEY = ''  # Replace with your Secret Access Key
AWS_REGION=""


# Initialize AWS Textract Client
textract_client = boto3.client(
    'textract',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Sample departments for categorization
departments = {
    "Infrastructure": ["road", "bridge", "transport", "construction"],
    "Health": ["hospital", "doctor", "medicine", "healthcare"],
    "Education": ["school", "teacher", "university", "college"],
    "Public Safety": ["police", "crime", "fire", "emergency"],
}

# Keywords for urgency detection
urgent_keywords = {"emergency", "immediate", "urgent", "critical", "danger"}

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

def categorize_petition(petition_text):
    words = petition_text.lower().split()
    for department, keywords in departments.items():
        if any(word in words for word in keywords):
            return department
    return "General"

def is_urgent(petition_text):
    words = set(petition_text.lower().split())
    return any(word in words for word in urgent_keywords)

def find_similar_petitions(petition_text, past_petitions):
    if not past_petitions:
        return None
    
    texts = [petition_text] + [p['text'] for p in past_petitions]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:].toarray())

    similar_indices = [i for i, score in enumerate(similarity_scores[0]) if score > 0.7]
    
    return [past_petitions[i] for i in similar_indices] if similar_indices else None

def process_petition(petition_text, petitions_db):
    petition_text = preprocess_text(petition_text)
    category = categorize_petition(petition_text)
    urgent = is_urgent(petition_text)
    similar_petitions = find_similar_petitions(petition_text, petitions_db)

    petition_record = {
        "id": len(petitions_db) + 1,
        "text": petition_text,
        "category": category,
        "urgent": urgent,
        "submitted_on": str(datetime.datetime.now().isoformat()),
        "status": "Pending",
        "official_notified": False,
        "updates": []
    }
    
    petitions_db.append(petition_record)
    return petition_record, similar_petitions

def send_reminders(petitions_db):
    today = datetime.datetime.now()
    for petition in petitions_db:
        submitted_date = datetime.datetime.fromisoformat(petition["submitted_on"])
        if (today - submitted_date).days > 7 and petition["status"] == "Pending":
            print(f"Reminder: Petition {petition['id']} needs attention!")

def update_petition_status(petitions_db, petition_id, status, update_message):
    for petition in petitions_db:
        if petition["id"] == petition_id:
            petition["status"] = status
            petition["updates"].append({"date": str(datetime.datetime.now().isoformat()), "message": update_message})
            return petition
    return None

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber"""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text.strip()

def extract_text_from_image(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    response = textract_client.detect_document_text(Document={"Bytes": image_bytes})
    extracted_text = "\n".join(
        block["Text"] for block in response["Blocks"] if block["BlockType"] == "LINE"
    )
    
    print("\n✅ Extracted Text:\n", extracted_text)
    return extracted_text.strip()

def process_uploaded_file(file_path):
    """Determine file type (PDF or image) and extract text accordingly"""
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        return extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or image.")

# Sample Execution
if __name__ == "__main__":
    petitions_db = []
    
    while True:
        print("\nUpload a petition file (PDF or Image) or type 'exit' to stop:")
        file_path = input().strip()
        
        if file_path.lower() == 'exit':
            break
        
        if not os.path.exists(file_path):
            print("File not found. Please enter a valid file path.")
            continue

        try:
            petition_text = process_uploaded_file(file_path)
            if not petition_text:
                print("No text extracted. Please check the file and try again.")
                continue

            petition_record, similar = process_petition(petition_text, petitions_db)

            print("\nProcessed Petition:")
            print(json.dumps(petition_record, indent=4))

            if similar:
                print("\nSimilar Petitions:")
                for sp in similar:
                    print(json.dumps(sp, indent=4))
        except Exception as e:
            print(f"Error processing file: {e}")
