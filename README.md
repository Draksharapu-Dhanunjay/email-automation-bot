# 📧 Email Automation Bot – HR Cold Outreach (Python)

A Python-based automation tool designed to send professional cold emails with resume attachments to HR and recruitment teams in a **safe, controlled, and ethical manner**.

This project helps job seekers automate repetitive email outreach while following best practices such as rate limiting, logging, and secure authentication.

---

## 📌 Project Motivation

Manually sending resumes to hundreds of recruiters is time-consuming and error-prone.  
This project was built to:

- Automate repetitive HR outreach
- Maintain professionalism and consistency
- Avoid spam behavior using controlled limits
- Practice real-world Python automation and Git workflows

---

## 🚀 Features

- 📄 Reads HR email IDs from a CSV file
- ✉️ Uses a reusable plain-text email template
- 📎 Automatically attaches a resume (PDF)
- 🔐 Secure Gmail SMTP authentication using App Passwords
- ⏱️ Rate-limited email sending (configurable delay & limits)
- 📝 Logs sent and failed emails for tracking
- 🧪 Supports dry-run validation before live sending
- 🧹 Keeps sensitive data out of version control

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** pandas, smtplib, email.message
- **Email Service:** Gmail SMTP
- **Version Control:** Git & GitHub
- **IDE:** VS Code
- **OS Tested:** Windows

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
├── logs/
│   └── sent_emails.log      # Email send logs
│
├── email_template.txt       # Email subject + body
├── send_emails.py           # Main automation script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Protects sensitive data
```

---

## ⚙️ How It Works

1. HR email addresses are stored in a CSV file.
2. The email subject and body are loaded from a text template.
3. The script authenticates with Gmail using SMTP and an App Password.
4. Emails are sent one by one with configurable delays.
5. Each email’s status (sent/failed) is logged locally.

This design ensures **control, transparency, and safety**.

---

## 🔒 Security & Best Practices

- Gmail **App Passwords** used instead of account password
- Rate limiting to avoid spam flags
- Sensitive files excluded using `.gitignore`
- No hard-coded credentials in source code
- Logging enabled for audit and retry support

---

## 📈 Use Cases

- Job seekers automating HR outreach
- Python automation practice
- Learning SMTP & email workflows
- Foundation for AI-based personalization
- Resume / portfolio demonstration project

---

## 🔮 Future Enhancements

- Follow-up email automation
- Role-based or company-specific templates
- AI-generated personalized email content
- Resume–job description matching
- Web dashboard or GUI
- Migration to scalable services like AWS SES

---

## ⚠️ Disclaimer

This project is intended for **ethical and professional use only**.  
Users must comply with email service policies and avoid spam practices.

---

## 👤 Author

**Dhanunjay Draksharapu**

- GitHub: https://github.com/Draksharapu-Dhanunjay
- LinkedIn: https://www.linkedin.com/in/draksharapu-dhanunjay-9a564a3a0/

---

## 📜 License

MIT License
```
