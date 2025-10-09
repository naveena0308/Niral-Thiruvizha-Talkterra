import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD

def send_email(to_email, subject, body):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = to_email
        msg.set_content(body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print("❌ Email error:", e)

def send_confirmation_email(email, name, petition_id):
    body = f"""Dear {name},

Your petition has been successfully submitted.
Petition ID: {petition_id}

We will notify you when your grievance progresses.

Regards,
Grievance Cell"""
    send_email(email, "Petition Submission Confirmation", body)

def send_status_update_email(email, name, petition_id, status):
    body = f"""Dear {name},

The status of your petition (ID: {petition_id}) has been updated to: {status}.

Thank you for your patience.

Regards,
Grievance Cell"""
    send_email(email, "Petition Status Updated", body)
