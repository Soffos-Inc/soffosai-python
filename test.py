from soffos import Client
from soffos.common.constants import Services

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

ai_client = Client(api_key)
ai_client.service = Services.QUESTION_ANSWERING
ai_client.src = "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]"
ai_client.question = "What is a canid?"
ai_client.user = "MeAgain"
print(ai_client.get_response())
# print(f"CONTEXT: {ai_client.context}")

# l = dict
# src = {"e": 1}
# print(type(src))
# print(isinstance(src, l))