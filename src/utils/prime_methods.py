import os
import imaplib
import email
import re

from email.header import decode_header


def get_code_by_email(user_email: str, imap_email: str, imap_password: str ) -> str:
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

            for msg_id in message_ids[::-1]:
                status, message = mail.fetch(msg_id, "(RFC822)")

                if status == "OK":

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

                                if ("amazon.com: Intento de inicio de sesión".replace(" ", "") in new_subject) or ("amazon.com: Sign-in attempt".replace(" ", "") in new_subject) or ("amazon.com :Tentativedeconnexion" in new_subject):

                                    if email_message.is_multipart():
                                        for part in email_message.walk():
                                            if part.get_content_type() == "text/html":
                                                body = part.get_payload(decode=True).decode(
                                                    "utf-8", errors="ignore")
                                    else:
                                        body = email_message.get_payload(
                                            decode=True).decode("utf-8", errors="ignore")
                                        
                                    text = re.sub(r'<[^>]+>', '', body)

                                    code = re.findall(r'(\d{6})(?:\s|\n|$)', text)

                                    if code:
                                        print(f"Código: {code[-1]}")
                                        return code[-1]
                            

        else:
            status, messages = mail.search(
                None, f'(HEADER From "Amazon" TO "{user_email}" SINCE "26-Jun-2025")')
            
            if status == "OK":
                message_ids: list[str] = messages[0].split()

                for msg_id in message_ids[::-1]:
                    status, message = mail.fetch(msg_id, "(RFC822)")

                    if status == "OK":

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

                                if ("amazon.com: Intento de inicio de sesión".replace(" ", "") in new_subject) or ("amazon.com: Sign-in attempt".replace(" ", "") in new_subject) or ("amazon.com :Tentativedeconnexion" in new_subject):

                                    if email_message.is_multipart():
                                        for part in email_message.walk():
                                            if part.get_content_type() == "text/html":
                                                body = part.get_payload(decode=True).decode(
                                                    "utf-8", errors="ignore")
                                    else:
                                        body = email_message.get_payload(
                                            decode=True).decode("utf-8", errors="ignore")
                                        
                                    text = re.sub(r'<[^>]+>', '', body)

                                    code = re.findall(r'(\d{6})(?:\s|\n|$)', text)

                                    if code:
                                        print(f"Código: {code[-1]}")
                                        return code[-1]

    mail.close()



def call_get_prime_session_code(user_email: str) -> str:
    emails: list[str] = [
        os.getenv("FOURTH_EMAIL")]
    passwords: list[str] = [
        os.getenv("FOURTH_PASSWORD")]
    

    for email, password in zip(emails, passwords):
        print(email)

        code = get_code_by_email(user_email, email, password)

        if code:
            return code