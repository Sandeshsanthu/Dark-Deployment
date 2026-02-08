import os
from unleash import UnleashClient

client = UnleashClient(
    url=os.getenv("UNLEASH_URL"),
    app_name="ml-api"
)

client.initialize_client()

def is_enabled(flag):
    return client.is_enabled(flag)
