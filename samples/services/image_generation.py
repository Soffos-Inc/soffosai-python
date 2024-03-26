import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"

service1 = SoffosAIServices.ImageGenerationService()
output = service1(
    user="franco",
    prompt="a picture of Ironman, sewing dresses.",
    quality="hd",
    quantity=1,
    size="1024x1024"
)
print(json.dumps(output, indent=4))