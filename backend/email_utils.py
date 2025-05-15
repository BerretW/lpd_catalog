import smtplib
from email.mime.text import MIMEText
from backend.config import load_config

config = load_config()["email"]

def send_email(to: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["sender"]
    msg["To"] = to

    with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
        server.starttls()
        server.login(config["username"], config["password"])
        server.send_message(msg)
