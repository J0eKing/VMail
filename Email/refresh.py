import imaplib
import email
import pyttsx3
import smtplib
import datetime
import sys


class Email:
    def __init__(self, user, passw, server="imap.gmail.com"):
        self.user = user
        self.passw = passw
        self.imap = imaplib.IMAP4_SSL(server)
        self.subject = []
        self.body = []
        self.sender = []
        self.attachment = []
        self.s = pyttsx3.init()
        self.time = []
        self.e = pyttsx3.init()

    def login(self):
        self.imap.login(self.user, self.passw)

    def get_new_emails(self):
        conn = self.imap
        conn.select("INBOX")
        rv, data = conn.search(None, "(UNSEEN)")

        for num in data[0].split():
            rv, data = conn.fetch(num, "(RFC822)")
            raw = data[0][1]
            b = email.message_from_string(str(raw, "utf8"))
            self.sender.append(b["From"])
            self.subject.append(b["Subject"])
            time = str(raw, "utf8").split("\n")[2].rstrip()
            self.time.append(time)

            # get body
            body = ""
            if b.is_multipart():
                for part in b.walk():
                    ctype = part.get_content_type()
                    cdispo = str(part.get("Content-Disposition"))

                    if ctype == "text/plain" and 'attachment' not in cdispo:
                        body = part.get_payload(decode=True)
                        break
            else:
                body = b.get_payload(decode=True)

            self.body.append(str(body, "utf8"))
            # set seen
            for response_part in data:
                if isinstance(response_part, tuple):
                    typ, data = conn.store(num, '+FLAGS', '\\Seen')
            all_attachments = []
            # check for attachments
            print(num)
            if b.is_multipart():
                for part in b.walk():
                    cdispo = part.get("Content-Disposition")
                    if cdispo is not None:
                        attachment_data = part.get_payload()
                        ctype = part.get_content_type()
                        attachment_name = part.get_filename()
                        attachment = [attachment_name, ctype, attachment_data]
                        all_attachments.append(attachment)

            self.attachment.append(all_attachments)

    def close(self):
        self.imap.close()
        self.imap.logout()

    def say(self):
        num = len(self.sender)
        if num == 0:
            self.e.say("You have no new emails")
            self.e.runAndWait()
        else:
            self.e.say("You have " + str(num) + " new emails")
            self.e.runAndWait()

    def send(self, to, subject, msg):
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.ehlo()
        s.starttls()

        s.login(self.user, self.passw)

        message = "\r\n".join([
            "From: " + self.user,
            "To: " + to,
            "Subject: " + subject,
            "",
            msg
        ])
        s.sendmail(self.user, to, message)

