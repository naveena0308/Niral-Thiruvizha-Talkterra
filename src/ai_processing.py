import os
import json
import re
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import GOOGLE_API_KEY, TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=GOOGLE_API_KEY)

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    tesseract_lang = 'tam+eng'

    if ext == ".pdf":
        images = convert_from_path(path)
        text = ''.join(pytesseract.image_to_string(img, lang=tesseract_lang) for img in images)
    else:
        img = Image.open(path).convert("RGB")
        text = pytesseract.image_to_string(img, lang=tesseract_lang)
    return text.strip()

def analyze_text(text):
    prompt = PromptTemplate(
        input_variables=["petition"],
        template="""
You are an AI assistant. Analyze the following petition and return a JSON object with:
- category (e.g., Water, Electricity, Health, Roads)
- is_urgent (true/false)
- summary (1–2 sentences)

Petition: {petition}
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"petition": text})
    cleaned = re.sub(r"json|```", "", response).strip()

    try:
        return json.loads(cleaned)
    except:
        return {"category": "Unknown", "is_urgent": False, "summary": "Could not extract"}
