from soffos import Client
from soffos.common.constants import Services

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

franco_ai = Client(apikey=api_key)

franco_ai.service = Services.QUESTION_ANSWERING
franco_ai.src = "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]"
franco_ai.question = "What are the other terms for dog"
franco_ai.user = "IamFranco"
response = franco_ai.get_response()

print(response)
# print(franco_ai.context)
print(type(franco_ai.raw_response))