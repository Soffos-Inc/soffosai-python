from soffos import Client, Services
from soffos.client import clients
from apikey import api_key


# ai_client = Client(api_key)
# ai_client.service = Services.AMBIGUITY_DETECTION
ai_client = clients.AmbiguityDetectionClient(apikey=api_key)
ai_client.user = "Me Again"
ai_client.src = "I saw her duck."
response = ai_client.get_response()
print(response.raw_response)
