import json
from soffosai import *


service = TagGenerationService()
output = service(
    user = "client_id",
    text = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series...",
    n = 3
)
print(json.dumps(output, indent=4))
