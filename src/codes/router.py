from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from src.codes.schemas import SessionCodes

from src.codes.crud import *


codes_router = APIRouter()


@codes_router.post("/disney/session_code/", tags=["disney_codes"])
def get_code_email(user_input: SessionCodes) -> JSONResponse:

    if user_input.password not in (os.getenv("DISNEY_PASSWORDS_CODE").replace(" ", "").replace("[", "").replace("]", "")).split(","):
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        code = get_code_email_by_email(email=user_input.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not code:
        raise HTTPException(status_code=404, detail="Code not found")

    return JSONResponse(content={
        "code": code,
    }, status_code=status.HTTP_200_OK)


@codes_router.get("/netflix/temporal_access/{email}", tags=["netflix_codes"])
def get_temporal_access(email: str) -> JSONResponse:

    try:

        link = get_temporal_access_code_by_email(email=email)

        if not link:
            raise HTTPException(status_code=404, detail="Link not found")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"link": link}, status_code=status.HTTP_200_OK)


@codes_router.get("/netflix/home_code/{email}", tags=["netflix_codes"])
def get_home_code(email: str) -> JSONResponse:

    try:
        link = get_home_code_by_email(email=email)

        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"link": link}, status_code=status.HTTP_200_OK)


@codes_router.post("/netflix/session_code/", tags=["netflix_codes"])
def get_session_code(user_input: SessionCodes) -> JSONResponse:

    if user_input.password not in (os.getenv("NETFLIX_PASSWORDS_CODE").replace(" ", "").replace("[", "").replace("]", "")).split(","):
        raise HTTPException(status_code=401, detail="Unauthorized")

    code = netflix_session_code_by_email(email=user_input.email)

    if not code:
        raise HTTPException(status_code=404, detail="Code not found")

    return JSONResponse(content={"code": code}, status_code=status.HTTP_200_OK)


@codes_router.post("/netflix/password_reset/", tags=["netflix_codes"])
def reset_password(user_input: SessionCodes) -> JSONResponse:

    if user_input.password not in (os.getenv("NETFLIX_PASSWORDS_CODE").replace(" ", "").replace("[", "").replace("]", "")).split(","):
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        link = get_reset_password_by_email(email=user_input.email)

        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"link": link}, status_code=status.HTTP_200_OK)


@codes_router.get("/netflix/new_session/{email}", tags=["netflix_codes"])
def new_session(email: str) -> JSONResponse:

    try:
        link = get_new_session_by_email(email=email)

        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"link": link}, status_code=status.HTTP_200_OK)


@codes_router.post("/prime/session_code/", tags=["prime_codes"])
def get_prime_code(user_input: SessionCodes) -> JSONResponse:

    if user_input.password not in (os.getenv("PRIME_PASSWORDS_CODE").replace(" ", "").replace("[", "").replace("]", "")).split(","):
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        code = get_prime_code_by_email(email=email)

        if not code:
            raise HTTPException(status_code=404, detail="Code not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"code": code}, status_code=status.HTTP_200_OK)


@codes_router.post("/hbo/session_code/", tags=["hbo_codes"])
def get_hbo_code(user_input: SessionCodes) -> JSONResponse:

    if user_input.password not in (os.getenv("HBO_PASSWORDS_CODE").replace(" ", "").replace("[", "").replace("]", "")).split(","):
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        code = get_hbo_code_by_email(email=email)

        if not code:
            raise HTTPException(status_code=404, detail="Code not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"code": code}, status_code=status.HTTP_200_OK)
