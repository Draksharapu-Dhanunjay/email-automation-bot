# 📧 Email Automation Bot – HR Cold Outreach (Python)

A Python-based automation tool designed to send professional cold emails with resume attachments to HR and recruitment teams in a **safe, controlled, and ethical manner**.

This project helps job seekers automate repetitive email outreach while following industry best practices such as **rate limiting, logging, validation, and secure authentication**.

---

## 📌 Project Motivation

Manually sending resumes to hundreds of recruiters is time-consuming and error-prone.
This project was built to:

* Automate repetitive HR outreach
* Maintain professionalism and consistency
* Avoid spam behavior using controlled limits
* Practice real-world Python automation, security, and Git workflows

---

## 🚀 Features

* 📄 Reads HR email IDs from a CSV file
* ✉️ Uses a reusable plain-text email template
* 📎 Automatically attaches a resume (PDF)
* 🔐 Secure Gmail SMTP authentication using App Passwords
* ⏱️ Rate-limited email sending (configurable delay & limits)
* 📝 Logs sent and failed emails for tracking
* 🧪 Supports **dry-run mode** for safe testing
* 🧹 Keeps sensitive data out of version control

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** pandas, smtplib, email.message
* **Email Service:** Gmail SMTP
* **Version Control:** Git & GitHub
* **IDE:** VS Code
* **OS Tested:** Windows

---

## 📂 Project Structure

```
email-automation-bot/
│
├── data/
│   └── hr_emails.csv        # HR email list (ignored in Git)
│
├── resume/
│   └── Resume_Sample.pdf    # Placeholder resume
│
├── email_template.txt       # Email body template
├── send_emails.py           # Main automation script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Protects sensitive data
```

---

## ⚙️ How It Works

1. HR email addresses are loaded from a CSV file.
2. The email body is read from a reusable template.
3. Credentials are securely loaded via environment variables.
4. The script connects to Gmail SMTP using an App Password.
5. Emails are processed sequentially with rate limits.
6. Each email’s status is logged for transparency.

This design ensures **control, reliability, and safety**.

---

## ▶ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/email-automation-bot.git
cd email-automation-bot
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

```bash
set SENDER_EMAIL=your_email@gmail.com
set APP_PASSWORD=your_gmail_app_password
```

### 5️⃣ Run in dry-run mode (recommended)

```bash
python send_emails.py
```

Set `DRY_RUN = False` only after verification.

---

## 🔒 Security & Best Practices

* Gmail **App Passwords** used instead of account passwords
* Credentials loaded via **environment variables**
* Rate limiting to prevent spam behavior
* Dry-run mode to prevent accidental sends
* Input validation on CSV structure
* Sensitive files excluded via `.gitignore`

---

## 📈 Use Cases

* Job seekers automating HR outreach
* Python automation learning project
* SMTP and email workflow practice
* Foundation for AI-driven personalization
* Resume & portfolio showcase

---

## 🔮 Future Enhancements

* Follow-up email automation
* Role-based or company-specific templates
* AI-generated personalized emails
* Resume–job description matching
* Web dashboard or GUI
* Migration to scalable email services (AWS SES, SendGrid)

---

## ⚠️ Disclaimer

This project is intended for **ethical and professional use only**.
Users must comply with email service policies and avoid spam practices.

---

## 👤 Author

**Dhanunjay Draksharapu**

* GitHub: [https://github.com/Draksharapu-Dhanunjay](https://github.com/Draksharapu-Dhanunjay)
* LinkedIn: [https://www.linkedin.com/in/draksharapu-dhanunjay-9a564a3a0/](https://www.linkedin.com/in/draksharapu-dhanunjay-9a564a3a0/)

---

## 📜 License

This project is licensed under the **MIT License**.

---

