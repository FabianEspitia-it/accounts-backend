import os
import imaplib
import email
import re

from email.header import decode_header


def get_netflix_code_email(user_email: str, email_subject: str, imap_email: str, imap_password: str) -> str:

    mail = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"))

    mail.login(imap_email, imap_password)

    mail.select("inbox")

    status, messages = mail.search(
        None, f'(FROM "{user_email}") SINCE "26-Jun-2025"')

    if status == "OK":

        message_ids: list[str] = messages[0].split()

        if message_ids != []:

            for msg_id in message_ids[::-1]:

                status, message = mail.fetch(msg_id, "(RFC822)")

                if status == "OK":
                    for response in message:
                        if isinstance(response, tuple):
                            email_message = email.message_from_bytes(
                                response[1])

                            subject, encoding = decode_header(
                                email_message["Subject"])[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(
                                    encoding if encoding else "utf-8")

                            new_subject: str = subject.replace(
                                " ", "").replace("RV:", "").replace("FW:", "").replace("هدایت:", "")
                            


                            if email_subject in new_subject:

                                if email_message.is_multipart():
                                    for part in email_message.walk():
                                        if part.get_content_type() == "text/plain":
                                            body = part.get_payload(decode=True).decode(
                                                "utf-8", errors="ignore")
                                else:
                                    body = email_message.get_payload(
                                        decode=True).decode("utf-8", errors="ignore")

                                pattern = None

                               

                                if email_subject == "Tu código de acceso temporal de Netflix".replace(" ", ""):

                                    pattern = r'https://www\.netflix\.com/account/travel/verify\?nftoken=[\w-]+.*'
                                elif email_subject == "Completa tu solicitud de restablecimiento de contraseña".replace(" ", ""):
                                    pattern = r'https:\/\/www\.netflix\.com\/password\?g=[\w-]+(?:&[\w%=-]+)*'
                                elif email_subject == "Netflix: Nueva solicitud de inicio de sesión".replace(" ", ""):
                                    pattern = r'https:\/\/www\.netflix\.com\/ilum\?code=[A-Za-z0-9]+'
                                else:
                                    pattern = r'https://www\.netflix\.com/account/update-primary-location\?nftoken=[\w\+\/-]+.*'

                                match = re.search(pattern, body)

                                if match:

                                    link = match.group(0).replace(
                                        ">", "").replace("]", "").replace("\r", "")

                                    return link

                                else:
                                    return None

                            else:
                                print("No se encontró el asunto del correo")
                                continue
        else:
            status, messages = mail.search(
                None, f'(FROM "info@account.netflix.com" TO "{user_email}" SINCE "26-Jun-2025")')

            if status == "OK":

                message_ids = messages[0].split()

                for msg_id in message_ids[::-1]:

                    status, message = mail.fetch(msg_id, "(RFC822)")

                    if status == "OK":
                        for response in message:
                            if isinstance(response, tuple):
                                email_message = email.message_from_bytes(
                                    response[1])

                                subject, encoding = decode_header(
                                    email_message["Subject"])[0]
                                if isinstance(subject, bytes):
                                    subject = subject.decode(
                                        encoding if encoding else "utf-8")

                                new_subject: str = subject.replace(
                                    " ", "").replace("RV:", "").replace("FW:", "").replace("هدایت:", "")

                                if email_subject in new_subject:

                                    if email_message.is_multipart():
                                        for part in email_message.walk():
                                            if part.get_content_type() == "text/plain":
                                                body = part.get_payload(decode=True).decode(
                                                    "utf-8", errors="ignore")
                                    else:
                                        body = email_message.get_payload(
                                            decode=True).decode("utf-8", errors="ignore")

                                    pattern = None

                                    if email_subject == "Tu código de acceso temporal de Netflix".replace(" ", ""):

                                        pattern = r'https://www\.netflix\.com/account/travel/verify\?nftoken=[\w-]+.*'
                                    elif email_subject == "Completa tu solicitud de restablecimiento de contraseña".replace(" ", ""):
                                        pattern = r'https:\/\/www\.netflix\.com\/password\?g=[\w-]+(?:&[\w%=-]+)*'
                                    elif email_subject == "Netflix: Nueva solicitud de inicio de sesión".replace(" ", ""):
                                        pattern = r'https:\/\/www\.netflix\.com\/ilum\?code=[A-Za-z0-9]+'
                                    else:
                                        pattern = r'https://www\.netflix\.com/account/update-primary-location\?nftoken=[\w\+\/-]+.*'

                                    match = re.search(pattern, body)

                                    if match:

                                        link = match.group(0).replace(
                                            ">", "").replace("]", "").replace("\r", "")

                                        return link

                                    else:
                                        return None

                                else:
                                    print("No se encontró el asunto del correo")
                                    continue

    mail.close()


def call_get_netflix_code_email(user_email: str, email_subject: str) -> str:

    emails: list[str] = [
        os.getenv("FIFTH_EMAIL"), os.getenv("FOURTH_EMAIL"), os.getenv("EIGHTH_EMAIL"), os.getenv("SEVENTH_EMAIL"), os.getenv("FIRST_EMAIL"), os.getenv("SECOND_EMAIL"), os.getenv("THIRD_EMAIL"), os.getenv("SIXTH_EMAIL")]
    passwords: list[str] = [
        os.getenv("FIFTH_PASSWORD"), os.getenv("FOURTH_PASSWORD"), os.getenv("EIGHTH_PASSWORD"), os.getenv("SEVENTH_PASSWORD"), os.getenv("FIRST_PASSWORD"), os.getenv("SECOND_PASSWORD"), os.getenv("THIRD_PASSWORD"), os.getenv("SIXTH_PASSWORD")]

    for email, password in zip(emails, passwords):
        print(email, password)
        link = get_netflix_code_email(
            user_email=user_email, email_subject=email_subject, imap_email=email, imap_password=password)

        if link:
            return link


def get_netflix_session_code(user_email: str, imap_email: str, imap_password: str) -> str:
    mail = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"))

    mail.login(imap_email, imap_password)

    mail.select("inbox")

    status, messages = mail.search(
        None, f'(FROM "{user_email}") SINCE "26-Jun-2025"')

    if status == "OK":

        message_ids: list[str] = messages[0].split()

        if message_ids != []:

            for msg_id in message_ids[::-1]:
                status, message = mail.fetch(msg_id, "(RFC822)")

                if status == "OK":
                    for response in message:
                        if isinstance(response, tuple):
                            email_message = email.message_from_bytes(
                                response[1])

                            subject, encoding = decode_header(
                                email_message["Subject"])[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(
                                    encoding if encoding else "utf-8")

                            new_subject: str = subject.replace(
                                " ", "").replace("RV:", "").replace("FW:", "")

                            if "Tu código de inicio de sesión".replace(" ", "") in new_subject:

                                if email_message.is_multipart():
                                    for part in email_message.walk():
                                        if part.get_content_type() == "text/plain":
                                            body = part.get_payload(decode=True).decode(
                                                "utf-8", errors="ignore")
                                else:
                                    body = email_message.get_payload(
                                        decode=True).decode("utf-8", errors="ignore")

                                code = re.findall(
                                    r'(\d{4})(?:\s|\n|$)', body)

                                if code:
                                    print(code)
                                    return code[1]

                                else:
                                    return None

        else:
            status, messages = mail.search(
                None, f'(FROM "info@account.netflix.com" TO "{user_email}" SINCE "26-Jun-2025")')

            if status == "OK":

                message_ids: list[str] = messages[0].split()

                for msg_id in message_ids[::-1]:

                    status, message = mail.fetch(msg_id, "(RFC822)")

                    if status == "OK":
                        for response in message:
                            if isinstance(response, tuple):
                                email_message = email.message_from_bytes(
                                    response[1])

                                subject, encoding = decode_header(
                                    email_message["Subject"])[0]
                                if isinstance(subject, bytes):
                                    subject = subject.decode(
                                        encoding if encoding else "utf-8")

                                new_subject: str = subject.replace(
                                    " ", "").replace("RV:", "").replace("FW:", "")

                                if "Tu código de inicio de sesión".replace(" ", "") in new_subject:

                                    if email_message.is_multipart():
                                        for part in email_message.walk():
                                            if part.get_content_type() == "text/plain":
                                                body = part.get_payload(decode=True).decode(
                                                    "utf-8", errors="ignore")
                                    else:
                                        body = email_message.get_payload(
                                            decode=True).decode("utf-8", errors="ignore")

                                    code = re.findall(
                                        r'(\d{4})(?:\s|\n|$)', body)

                                    if code:
                                        print(code)
                                        return code[0]

                                    else:
                                        return None

    mail.close()


def call_get_netflix_session_code(user_email: str) -> str:

    emails: list[str] = [
        os.getenv("FIFTH_EMAIL"), os.getenv("FOURTH_EMAIL"), os.getenv("EIGHTH_EMAIL"), os.getenv("SEVENTH_EMAIL"), os.getenv("FIRST_EMAIL"), os.getenv("SECOND_EMAIL"), os.getenv("THIRD_EMAIL"), os.getenv("SIXTH_EMAIL")]
    passwords: list[str] = [
        os.getenv("FIFTH_PASSWORD"), os.getenv("FOURTH_PASSWORD"), os.getenv("EIGHTH_PASSWORD"), os.getenv("SEVENTH_PASSWORD"), os.getenv("FIRST_PASSWORD"), os.getenv("SECOND_PASSWORD"), os.getenv("THIRD_PASSWORD"), os.getenv("SIXTH_PASSWORD")]

    for email, password in zip(emails, passwords):
        print(email)
        code = get_netflix_session_code(
            user_email=user_email, imap_email=email, imap_password=password)

        if code:
            return code
