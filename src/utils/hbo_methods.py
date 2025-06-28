import os
import imaplib
import email
import re

from email.header import decode_header


def get_hbo_code_by_email(user_email: str, imap_email: str, imap_password: str) -> str:
    mail = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"), port=993)

    mail.login(imap_email, imap_password)

    mail.select("inbox")

    print(user_email)

    status, messages = mail.search(
        None, f'(FROM "{user_email}" SINCE "26-Jun-2025")'
    )

    if status == "OK":

        message_ids: list[str] = messages[0].split()

        if message_ids != []:


            print("Estoy en el if")

            status, message = mail.fetch(message_ids[::-1], "(RFC822)")

            for response in message:

                if isinstance(response, tuple):

                    email_message = email.message_from_bytes(response[1])

                    subject, encoding = decode_header(
                        email_message["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(
                            encoding if encoding else "utf-8")
                        
                        print(subject)

                        new_subject: str = subject.replace(" ", "")

                        if ("Urgente: Tu").replace(" ", "") in new_subject:

                            if email_message.is_multipart():
                                for part in email_message.walk():
                                    if part.get_content_type() == "text/html":
                                        body = part.get_payload(decode=True).decode(
                                            "utf-8", errors="ignore")
                            else:
                                body = email_message.get_payload(
                                    decode=True).decode("utf-8", errors="ignore")
                                
                            text = re.sub(r'<[^>]+>', '', body)
                            code = re.search(r'\b\d{6}\b', text)

                            if code:
                                return code.group(0)
                            
        else: 
            status, messages = mail.search(
                None, f'(HEADER From "Max" TO "{user_email}" SINCE "26-Jun-2025")')
            if status == "OK":
                message_ids: list[str] = messages[0].split()

                if message_ids != []:
                    status, message = mail.fetch(message_ids[::-1], "(RFC822)")

                    for response in message:

                        if isinstance(response, tuple):

                            email_message = email.message_from_bytes(response[1])

                            subject, encoding = decode_header(
                                email_message["Subject"])[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(
                                    encoding if encoding else "utf-8")
                                
                                print("Estoy aquí")
                                
                                print(subject)

                                new_subject: str = subject.replace(" ", "")

                                if ("Urgente: Tu").replace(" ", "") in new_subject:
                                    print("Entré al urgente")
                                    if email_message.is_multipart():

                                        print("Estoy en multipart")
                                        for part in email_message.walk():
                                            if part.get_content_type() == "text/html":
                                                body = part.get_payload(decode=True).decode(
                                                    "utf-8", errors="ignore")
                                    else:

                                        print("Estoy en else")
                                        body = email_message.get_payload(
                                            decode=True).decode("utf-8", errors="ignore")
                                        
                                    code = re.findall(
                                        r'<b>(\d{6})</b>', body)

                                    print(code)

                                    if code:
                                        return "".join(code)
                                    
    mail.close()


def call_get_hbo_code_by_email(user_email: str) -> str:
    emails: list[str] = [
        os.getenv("EIGHTH_EMAIL"), os.getenv("FIFTH_EMAIL"), os.getenv("FOURTH_EMAIL"), os.getenv("SEVENTH_EMAIL"), os.getenv("FIRST_EMAIL"), os.getenv("SECOND_EMAIL"), os.getenv("THIRD_EMAIL"), os.getenv("SIXTH_EMAIL")]
    passwords: list[str] = [
        os.getenv("EIGHTH_PASSWORD"), os.getenv("FIFTH_PASSWORD"), os.getenv("FOURTH_PASSWORD"), os.getenv("SEVENTH_PASSWORD"), os.getenv("FIRST_PASSWORD"), os.getenv("SECOND_PASSWORD"), os.getenv("THIRD_PASSWORD"), os.getenv("SIXTH_PASSWORD")]

    for email, password in zip(emails, passwords):

        print(email, password)

        
        code = get_hbo_code_by_email(
            user_email=user_email, imap_email=email, imap_password=password)

        if code:
            return code