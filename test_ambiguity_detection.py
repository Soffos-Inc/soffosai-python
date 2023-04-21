from soffos import Client, Services
from soffos.client import clients

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

# ai_client = Client(api_key)
# ai_client.service = Services.AMBIGUITY_DETECTION
ai_client = clients.AmbiguityDetectionClient(apikey=api_key)
ai_client.user = "Me Again"
ai_client.src = "I saw her duck."
ai_client.get_response()
print(ai_client.response)
