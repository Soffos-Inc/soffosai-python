import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.LanguageDetectionService()
output = service("client_user_id", "φιλόσοφος, που θεωρείται ο ιδρυτής της Δυτικής φιλοσοφίας και")
print(json.dumps(output, indent=4))
