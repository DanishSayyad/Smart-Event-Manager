from datetime import datetime
import pandas as pd

def getMails(email, file_path="data/mails.csv"):
    mails = []
    df = pd.read_csv(file_path)
    for _, row in df[df["to"] == email].iterrows():
        mail = Mail(
            mail_to=row["to"],
            subject=row["subject"],
            body=row["body"],
            date=row["date"],
            time=row["time"]
        )
        mails.append(mail)
    return mails

class Mail:
    def __init__(self, mail_to, subject, body, date=None, time=None):
        now = datetime.now()
        self.date = date if date else now.strftime("%d/%m/%Y")
        self.time = time if time else now.strftime("%H:%M")
        self.mail_to = mail_to
        self.subject = subject
        self.body = body

    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "subject": self.subject,
            "body": self.body
        }

    def displayMail(self):
        print(f"--- Mail ---")
        print(f"Date: {self.date}  Time: {self.time}")
        print(f"From: Smart Event Manager")
        print(f"Subject: {self.subject}")
        print(f"Body:\n{self.body}")
        print()
