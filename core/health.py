from core.database import check_database

async def system_health():
    db_status = await check_database()

    return {
        "service": "FinSight API",
        "status": "online",
        "database": "connected" if db_status else "not_configured_or_unavailable"
    }
