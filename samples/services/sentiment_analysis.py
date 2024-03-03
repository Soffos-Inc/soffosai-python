import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.SentimentAnalysisService()
output = service(
    user = "client_id",
    text = "Avocado shake tastes great!"
)
print(json.dumps(output, indent=4))
