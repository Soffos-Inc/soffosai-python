import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.LogicalErrorDetectionService()
output = service(
    user = "client_user_id",
    text = "Nobody has found evidence that UFOs don't exist, therefore they must exist. Many people are saying that voter fraud is real, therefore it must be real."
)
print(json.dumps(output, indent=4))
