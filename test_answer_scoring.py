from soffos import Client, Services
from apikey import api_key


ai = Client(apikey=api_key)

ai.service = Services.ANSWER_SCORING
ai.src = {
  "context": "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
  "question": "How long ago did dogs first become domesticated?",
  "answer": "Between 14,000 and 29,000 years ago.",
  "user_answer": "20,000 years ago."
}
# ai.user_answer = "20,000 years ago."
ai.user = "me again"
response = ai.get_response()

print(response.raw_response)
