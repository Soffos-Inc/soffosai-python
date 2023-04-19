from soffos import Client, Services

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"
contradiction_ai =  Client(apikey=api_key)
contradiction_ai.service = Services.CONTRADICTION_DETECTION

contradiction_ai.src = "The source noted that the Shaheen-2, with a range of 2400 km, has never been tested by Pakistan. Pakistan has said that it performed several tests of its 2300 km-range Shaheen-2 missile in September 2004."
contradiction_ai.user = "Meeeee"
contradiction_ai.get_response()
print(contradiction_ai.response)
print(contradiction_ai.raw_response)