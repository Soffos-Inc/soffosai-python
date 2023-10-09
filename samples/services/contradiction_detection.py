import json
from soffosai import *


service = ContradictionDetectionService()
output = service(
    user = "client_user_id",
    text = "The source noted that the Shaheen-2, with a range of 2400 km, has never been tested by Pakistan. Pakistan has said that it performed several tests of its 2300 km-range Shaheen-2 missile in September 2004."
)
print(json.dumps(output, indent=4))
