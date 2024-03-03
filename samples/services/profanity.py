import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.ProfanityService()
output = service(
    user = "client_id",
    text = "Your look like shit on your shirt! Fucking go home and change."
)
print(json.dumps(output, indent=4))
