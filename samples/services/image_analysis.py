import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"

service1 = SoffosAIServices.ImageAnalysisService()
output = service1(
    user="franco",
    prompt="Estimate the number of fruits per kind.",
    image_url="https://www.flowerchimp.com.ph/cdn/shop/products/Large._1946x.jpg"    
)
print(json.dumps(output, indent=4))