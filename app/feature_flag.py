import os
import logging
from UnleashClient import UnleashClient

UNLEASH_URL = os.getenv("UNLEASH_URL")
UNLEASH_APP_NAME = os.getenv("UNLEASH_APP_NAME", "dark-demo")

_client: UnleashClient | None = None

def init_unleash() -> None:
    global _client
    if not UNLEASH_URL:
        logging.warning("UNLEASH_URL not set; flags defaulting.")
        return

    headers = {"Authorization": UNLEASH_API_TOKEN} if UNLEASH_API_TOKEN else None

    _client = UnleashClient(
        url=UNLEASH_URL,
        app_name=UNLEASH_APP_NAME,
        instance_id=UNLEASH_INSTANCE_ID,
        custom_headers=headers,
        backup_file="unleash-backup.json",
    )
    _client.initialize_client()

def shutdown_unleash() -> None:
    global _client
    if _client:
        _client.destroy()
        _client = None

def is_enabled(flag: str, default: bool = False, context: dict | None = None) -> bool:
    if not _client:
        return default
    return _client.is_enabled(flag, context=context or {}, default_value=default)
