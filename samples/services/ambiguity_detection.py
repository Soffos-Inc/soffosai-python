import json
from soffosai import *


service = AmbiguityDetectionService()
output = service(
    text = "I saw his duck.",
    sentence_overlap = False,
    sentence_split=1,
    user = "client_user_id"
)
print(json.dumps(output, indent=4))
