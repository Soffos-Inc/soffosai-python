import json
from soffosai import SoffosAIServices
import soffosai

soffosai.api_key = "<your API key>"

service = SoffosAIServices.ChatBotCreateService()
output = service("franco", "programmer", "francobot",)
print(json.dumps(output, indent=4))

service = SoffosAIServices.ChatBotService()
output = service("franco", "can you help me code javascript?", "046b5ea5691544d3b40aa70e34272b30", "franco", "open")
print(json.dumps(output, indent=4))