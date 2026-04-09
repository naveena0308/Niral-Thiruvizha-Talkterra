import sqlite3
import pandas as pd
from datetime import datetime
from config import DB_FILE

def create_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS petitions (
            petition_id TEXT PRIMARY KEY,
            filename TEXT,
            submitted_text TEXT,
            extracted_text TEXT,
            category TEXT,
            is_urgent BOOLEAN,
            summary TEXT,
            petitioner_name TEXT,
            email TEXT,
            phone TEXT,
            status TEXT DEFAULT 'Received',
            last_updated TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_petition(data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO petitions (
            petition_id, filename, submitted_text, extracted_text, category,
            is_urgent, summary, petitioner_name, email, phone, status,
            last_updated, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["petition_id"], data["filename"], data["submitted_text"], data["extracted_text"],
        data["category"], data["is_urgent"], data["summary"],
        data["name"], data["email"], data["phone"],
        "Received", datetime.now().isoformat(), datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()

def update_status(petition_id, new_status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE petitions SET status = ?, last_updated = ? WHERE petition_id = ?",
                   (new_status, datetime.now().isoformat(), petition_id))
    conn.commit()
    conn.close()

def get_all_petitions():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM petitions ORDER BY timestamp DESC", conn)
    conn.close()
    return df
