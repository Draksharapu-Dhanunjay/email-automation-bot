# ==========================
# Imports
# ==========================
import os
import time
import smtplib
import pandas as pd
from email.message import EmailMessage
from pathlib import Path




# ==========================
# Configuration
# ==========================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

EMAIL_SUBJECT = "Application for Software / Java Backend Developer Opportunities"

EMAIL_DELAY_SECONDS = 5
MAX_EMAILS_PER_RUN = 20

DRY_RUN = True  # Set True to test without sending emails


# ==========================
# Helper Functions
# ==========================

def log(message: str, level: str = "INFO") -> None:
    """
    Simple logger with log levels.
    """
    print(f"[{level}] {message}")


def load_hr_emails(csv_path: str) -> list[str]:
    """
    Loads HR email addresses from a CSV file.

    Expected CSV format:
    email
    hr1@example.com
    hr2@example.com
    """
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.lower()

        if "email" not in df.columns:
            raise ValueError("CSV must contain 'email' column")

        emails = df["email"].dropna().tolist()
        return emails

    except Exception as e:
        log(f"Failed to load HR emails: {e}", level="ERROR")
        return []



def load_email_template(template_path: str) -> str:
    """
    Loads email body from a text file.
    """
    try:
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        log(f"Failed to load email template: {e}", level="ERROR")
        return ""



# ==========================
# Email Sending Logic
# ==========================

def build_email_message(
    recipient: str,
    subject: str,
    body: str,
    resume_path: str
) -> EmailMessage:
    """
    Builds an email message with a resume attachment.
    """
    message = EmailMessage()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    resume_file = Path(resume_path)

    if resume_file.exists():
        with open(resume_file, "rb") as file:
            message.add_attachment(
                file.read(),
                maintype="application",
                subtype="pdf",
                filename=resume_file.name
            )
    else:
       log(f"Resume not found at {resume_path}", level="WARNING")

    return message

def send_email(
    smtp_server: smtplib.SMTP,
    message: EmailMessage,
    recipient: str
) -> None:
    """
    Sends an email using an active SMTP connection.
    """
    if DRY_RUN:
        log(f"Email prepared for {recipient}", level="DRY RUN")
        return

    smtp_server.send_message(message)
    log(f"Email sent to {recipient}", level="SENT")


# ==========================
# Main Execution
# ==========================


def main():
    """
    Main execution function.
    """
    hr_emails = load_hr_emails("data/hr_emails.csv")
    email_body = load_email_template("email_template.txt")

    if not hr_emails:
        log("No HR emails found. Exiting.")
        return

    if not email_body:
        log("Email template is empty. Exiting.")
        return
    
    if DRY_RUN:
        log("DRY_RUN enabled. No emails will be sent.")
        for recipient in hr_emails:
            log(f"Email prepared for {recipient}", level="DRY RUN")
        return

    hr_emails = hr_emails[:MAX_EMAILS_PER_RUN]
    resume_path = "resume/Resume_Sample.pdf"


    try:
        log("Connecting to SMTP server...")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)

            for index, recipient in enumerate(hr_emails, start=1):
                log(f"Processing {index}/{len(hr_emails)}: {recipient}")

                message = build_email_message(
                    recipient=recipient,
                    subject=EMAIL_SUBJECT,
                    body=email_body,
                    resume_path=resume_path
                )

                send_email(server, message, recipient)

                if index < len(hr_emails):
                    time.sleep(EMAIL_DELAY_SECONDS)

        log("Email processing completed successfully.")

    except Exception as e:
        log(f"SMTP error occurred: {e}", level="ERROR")


if __name__ == "__main__":
    main()



