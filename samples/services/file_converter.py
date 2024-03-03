import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.FileConverterService()
output = service(user="client_user_id", file="location/of/file.pdf", normalize=1)
print(json.dumps(output, indent=4))
