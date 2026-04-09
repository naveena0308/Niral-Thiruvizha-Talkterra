# AI-Powered Petition Analyzer & Tracker

An intelligent grievance management system designed to streamline the process of petition submission, classification, and tracking through advanced automation and AI-driven insights.

---

### **Recognition & Achievement**
Selected among the **Top 1000 teams out of 10,000+** in the Tamil Nadu Government’s **Niral Thiruvizha 2.0 Hackathon**.  
📄 [View Achievement Certificate](assets/TNAS_S1000_1152_Naveena.pdf)

---

## Overview

The **AI-Powered Petition Analyzer & Tracker** is a robust grievance management solution built with Python, Streamlit, and Google Gemini AI. It automates the extraction, summarization, and classification of petitions, ensuring faster response times and more efficient resource allocation for governmental and organizational bodies.

## Key Features

- **Multimodal Petition Submission**: Supports direct text entry and scanned documents (PDF/Image) with high-accuracy OCR.
- **Intelligent Text Analysis**: Automatically categorizes petitions (e.g., Water, Health, Roads) and generates concise summaries using Gemini 1.5 Flash.
- **Urgency Detection**: AI-driven prioritization based on the content of the grievance.
- **Duplicate Detection**: Advanced similarity matching to identify and flag redundant submissions.
- **Comprehensive Admin Dashboard**: Centralized interface for status tracking, resolution monitoring, and data visualization.
- **Automated Communication**: Instant email notifications for submission confirmations and status updates via SMTP.

## Technical Architecture

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit |
| **OCR Engine** | Tesseract (Multi-language support) |
| **AI Model** | Google Gemini 1.5 Flash |
| **Framework** | LangChain |
| **Database** | SQLite |
| **Messaging** | Gmail SMTP Service |

## Project Structure

```text
Niral-Thiruvizha-Talkterra/
├── src/                  # Core application logic
│   ├── app.py            # Main Streamlit interface
│   ├── ai_processing.py  # AI and OCR integration
│   ├── database.py       # Persistence layer management
│   ├── email_utils.py    # Notification service
│   ├── utils.py          # Helper functions and similarity logic
│   └── config.py         # Environment and application settings
├── data/                 # Local database storage and temporary files
├── assets/               # Project documentation and certificates
├── requirements.txt      # Dependencies
└── README.md             # Technical documentation
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- Tesseract OCR (System-level installation)
- Google Gemini API Key
- Gmail App Password (for email notifications)

### Installation Steps

1. **Clone the Project**
   ```bash
   git clone https://github.com/yourusername/Niral-Thiruvizha-Talkterra.git
   cd Niral-Thiruvizha-Talkterra
   ```

2. **Environment Configuration**
   Create a `.env` file in the project root:
   ```ini
   GOOGLE_API_KEY=your_gemini_api_key
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   streamlit run src/app.py
   ```

---

## License

This project is licensed under the **MIT License**.

## Contributors

- **Naveena Natarajan** — Project Lead & System Architecture
- **Team Talkterra** — Research & Development

---
Developed as part of the **Niral Thiruvizha Hackathon initiative** by **Team Talkterra** ❤️ .
