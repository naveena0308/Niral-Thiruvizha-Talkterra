import os
import streamlit as st
import uuid
from database import create_db, save_petition, update_status, get_all_petitions
from ai_processing import extract_text, analyze_text
from email_utils import send_confirmation_email, send_status_update_email
from utils import find_similar_petitions
from datetime import datetime

def main():
    st.set_page_config(page_title="Petition Analyzer", layout="wide")
    st.title("AI-Powered Petition Analyzer & Tracker")

    create_db()

    with st.expander("Submit a Petition"):
        with st.form("form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            uploaded_file = st.file_uploader("📎 Upload PDF/Image", type=["pdf", "jpg", "jpeg", "png"])
            typed_text = st.text_area("Or type your petition")
            submitted = st.form_submit_button("Submit")

        if submitted:
            if not (name and email and phone):
                st.warning("All fields are required.")
                return
            if not uploaded_file and not typed_text.strip():
                st.warning("Upload a file or enter petition text.")
                return

            filename = uploaded_file.name if uploaded_file else "typed_text"
            path = f"temp_{filename}"
            if uploaded_file:
                with open(path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                extracted = extract_text(path)
                os.remove(path)
            else:
                extracted = typed_text.strip()

            analysis = analyze_text(extracted)
            df = get_all_petitions()
            prev_texts = dict(zip(df["petition_id"], df["extracted_text"]))
            repeated_id = find_similar_petitions(extracted, prev_texts)

            petition_id = str(uuid.uuid4())
            petition_data = {
                "petition_id": petition_id,
                "filename": filename,
                "submitted_text": typed_text if typed_text else None,
                "extracted_text": extracted,
                "category": analysis["category"],
                "is_urgent": analysis["is_urgent"],
                "summary": analysis["summary"],
                "name": name,
                "email": email,
                "phone": phone
            }

            save_petition(petition_data)
            send_confirmation_email(email, name, petition_id)

            st.success("Petition submitted successfully.")
            st.info(f"Petition ID: {petition_id}")
            if repeated_id:
                st.warning(f"⚠ Similar to previous petition ID: {repeated_id}")

    # ------------------- ADMIN -------------------
    st.markdown("---")
    st.subheader("Admin Dashboard")

    df = get_all_petitions()
    if not df.empty:
        selected = st.selectbox("Select Petition ID", df["petition_id"].tolist())
        row = df[df["petition_id"] == selected].iloc[0]
        st.write(f"*Summary*: {row['summary']}")
        st.write(f"*Category*: {row['category']}")
        st.write(f"*Urgent*: {row['is_urgent']}")
        st.write(f"*Current Status*: {row['status']}")
        st.write(f"*Submitted by*: {row['petitioner_name']}")

        new_status = st.selectbox("Update Status", ["Received", "In Progress", "Resolved"])
        if st.button("Apply Status Update"):
            update_status(row["petition_id"], new_status)
            send_status_update_email(row["email"], row["petitioner_name"], row["petition_id"], new_status)
            st.success("Status updated and email sent!")

        st.markdown("###All Petitions")
        st.dataframe(df)
    else:
        st.info("No petitions submitted yet.")

if __name__ == "__main__":
    main()
