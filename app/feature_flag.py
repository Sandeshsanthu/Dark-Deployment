from UnleashClient import UnleashClient
import os

client = UnleashClient(
    url=os.getenv("UNLEASH_URL"),
    app_name="ml-api"
)

client.initialize_client()

def is_enabled(flag):
    return client.is_enabled(flag)
