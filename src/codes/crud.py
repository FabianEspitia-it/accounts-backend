import time

from src.utils.disney_methods import *

from src.utils.netflix_methods import *

from src.utils.prime_methods import *

from src.utils.hbo_methods import *


def get_code_email_by_email(email: str) -> str:

    time.sleep(10)

    return call_get_disney_session_code(user_email=email)


def get_temporal_access_code_by_email(email: str):

    EMAIL_SUBJECT = "Tu código de acceso temporal de Netflix".replace(" ", "")

    time.sleep(8)

    return call_get_netflix_code_email(user_email=email, email_subject=EMAIL_SUBJECT)


def get_home_code_by_email(email: str) -> str:

    EMAIL_SUBJECT = "Importante:CómoactualizartuHogarconNetflix".replace(
        " ", "")

    time.sleep(8)
    return call_get_netflix_code_email(user_email=email, email_subject=EMAIL_SUBJECT)


def get_reset_password_by_email(email: str) -> str:

    EMAIL_SUBJECT = "Completatusolicitudderestablecimientodecontraseña".replace(
        " ", "")

    time.sleep(8)

    return call_get_netflix_code_email(user_email=email, email_subject=EMAIL_SUBJECT)


def netflix_session_code_by_email(email: str) -> str:

    time.sleep(8)

    return call_get_netflix_session_code(user_email=email)

def get_new_session_by_email(email: str) -> str:

    EMAIL_SUBJECT = "Netflix:Nuevasolicituddeiniciodesesión".replace(" ", "") 

    time.sleep(8)

    return call_get_netflix_code_email(user_email=email, email_subject=EMAIL_SUBJECT)


def get_prime_code_by_email(email: str) -> str:

    time.sleep(9)

    return call_get_prime_session_code(user_email=email)


def get_hbo_code_by_email(email: str) -> str:

    time.sleep(9)

    return call_get_hbo_code_by_email(user_email=email)
