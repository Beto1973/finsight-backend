from fastapi import Header, HTTPException
from config.settings import settings


def verify_platform_key(x_api_key: str = Header(None)):
    if settings.ENV == "development":
        return

    if not x_api_key or x_api_key != settings.PLATFORM_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
