# Niral-Thiruvizha-Talkterra

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

### AI-Powered Petition Analyzer & Tracker

An intelligent grievance management system that automates petition submission, classification, summarization, duplicate detection, tracking, and notification for efficient grievance redressal.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup Guide](#setup-guide)
- [Module Overview](#module-overview)
- [Database Schema](#database-schema)
- [Email Workflow](#email-workflow)
- [Example Workflow](#example-workflow)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

The **AI-Powered Petition Analyzer & Tracker** is an intelligent grievance management system built with **Streamlit**, **Tesseract OCR**, and **Google Gemini AI**. It automates the process of petition submission, classification, summarization, duplicate detection, tracking, and notification, ensuring faster and more efficient grievance redressal.

---

## Key Features

### Petition Submission
Accepts both text-based and scanned (PDF/Image) petitions with automatic text extraction using **Tesseract OCR** supporting Tamil and English.

### AI-Based Text Analysis
Categorizes petitions into predefined types such as Water, Health, Roads, Electricity, and more. Generates concise summaries and urgency tags using **Gemini 1.5 Flash**.

### Duplicate Petition Detection
Uses text similarity algorithms to identify previously submitted petitions and prevent redundant processing.

### Admin Dashboard
Intuitive Streamlit dashboard for tracking petition status and details. Supports petition updates, resolution marking, and detailed viewing.

### Automated Email Notifications
Sends petition submission confirmations and alerts petitioners automatically upon status updates.

---

## Technology Stack

| Component     | Technology              |
|---------------|-------------------------|
| Frontend      | Streamlit               |
| OCR           | Tesseract               |
| AI Model      | Google Gemini 1.5 Flash |
| NLP Framework | LangChain               |
| Database      | SQLite                  |
| Language      | Python 3.10+            |
| Email Service | Gmail SMTP              |

---

## Project Structure

```
petition_app/
│
├── app.py                # Main Streamlit interface
├── ai_processing.py      # OCR and AI-based analysis logic
├── database.py           # SQLite database management
├── email_utils.py        # Email notification handling
├── utils.py              # Helper utilities (similarity, formatting)
├── config.py             # Environment variables and configurations
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Setup Guide

### Prerequisites

- Python 3.10 or higher
- Tesseract OCR installed on your system
- Google Gemini API key
- Gmail account with App Password enabled

### Installation

**1. Clone the Repository**

```bash
git clone https://github.com/yourusername/Niral-Thiruvizha-Talkterra.git
cd Niral-Thiruvizha-Talkterra
```

**2. Create and Activate Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**

Create a `.env` file in the project root:

```ini
GOOGLE_API_KEY=your_google_api_key_here
EMAIL_SENDER=youremail@gmail.com
EMAIL_PASSWORD=your_email_app_password
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

**Important Notes:**
- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- For Gmail, use an **App Password** instead of your regular password
- Update `TESSERACT_PATH` to match your installation location

**5. Run the Application**

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`

---

## Module Overview

| Module             | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `config.py`        | Loads environment variables and application constants         |
| `database.py`      | Handles SQLite CRUD operations for petition management        |
| `ai_processing.py` | Performs OCR and AI-driven analysis using Gemini              |
| `email_utils.py`   | Manages email notifications and confirmations                 |
| `utils.py`         | Contains helper functions for text similarity and formatting  |
| `app.py`           | Main application connecting all components with Streamlit UI  |

### AI and NLP Component

| Component     | Details                                                        |
|---------------|----------------------------------------------------------------|
| **Model**     | Gemini 1.5 Flash                                               |
| **Framework** | LangChain (GoogleGenerativeAI Wrapper)                         |
| **Functions** | Text summarization, category classification, urgency detection |

---

## Database Schema

The application uses SQLite with the following schema:

| Column          | Type    | Description                                     |
|-----------------|---------|------------------------------------------------ |
| petition_id     | TEXT    | Unique identifier (UUID)                        |
| filename        | TEXT    | Uploaded file name                              |
| submitted_text  | TEXT    | Directly typed petition content                 |
| extracted_text  | TEXT    | OCR-extracted content                           |
| category        | TEXT    | AI-classified petition category                 |
| is_urgent       | BOOLEAN | Urgency indicator                               |
| summary         | TEXT    | AI-generated petition summary                   |
| petitioner_name | TEXT    | Petitioner's name                               |
| email           | TEXT    | Petitioner's email address                      |
| phone           | TEXT    | Contact number                                  |
| status          | TEXT    | Petition status (Received/In Progress/Resolved) |
| last_updated    | TEXT    | Timestamp of last update                        |
| timestamp       | TEXT    | Original submission timestamp                   |

---

## Email Workflow

| Event               | Recipient  | Description                                    |
|---------------------|------------|------------------------------------------------|
| Petition Submission | Petitioner | Sends confirmation with unique petition ID     |
| Status Update       | Petitioner | Sends notification when admin changes status   |

---

## Example Workflow

1. User uploads or types a petition through the web interface
2. OCR extracts text from uploaded images or PDFs
3. AI model classifies petition, generates summary, and assigns urgency
4. Petition data is stored in the SQLite database
5. Confirmation email is sent to the petitioner with petition ID
6. Admin reviews petitions and updates status through dashboard
7. System automatically notifies petitioner of status changes

---

## Future Enhancements

- Multi-language OCR support (Hindi, Telugu, Malayalam, etc.)
- Role-based admin authentication and user management
- Analytics dashboard with visualizations using Streamlit charts
- Sentiment and emotion analysis for better prioritization
- Integration with Power BI for advanced reporting
- Mobile application for easier access
- Real-time status tracking portal for petitioners

---

## Contributors

- **Naveena Natarajan** — Project Lead & AI Integration
- **Team Talkterra** — Development & Research Support

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project for academic or personal purposes.

---

## Support

For issues, questions, or contributions, please open an issue on GitHub or contact the project maintainers.

---

**Made with ❤️ by Team Talkterra**
