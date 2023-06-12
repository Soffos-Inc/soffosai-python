from soffos import Client, Services
from apikey import api_key


contradiction_ai =  Client(apikey=api_key)
contradiction_ai.service = Services.CONTRADICTION_DETECTION

contradiction_ai.src = "The source noted that the Shaheen-2, with a range of 2400 km, has never been tested by Pakistan. Pakistan has said that it performed several tests of its 2300 km-range Shaheen-2 missile in September 2004."
contradiction_ai.user = "Meeeee"
response = contradiction_ai.get_response()
print(response.response)
print(response.cost)