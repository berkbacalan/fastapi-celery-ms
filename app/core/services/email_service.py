from config import settings

def send_email(receiver_email: str, subject: str, message: str):
    sender_email = settings.EMAIL_SENDER
    password = settings.EMAIL_PASSWORD
    print(f"EMAIL SUCCESS. receiver_email:{receiver_email}. subject: {subject}. message: {message}")

