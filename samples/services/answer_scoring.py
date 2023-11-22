import json
import soffosai
from soffosai import *

soffosai.api_key = "Token 0d1d8cc5-ccd5-47dc-be99-a8153def24f3"
service = AnswerScoringService()
output = service(
    user = "client_user_id",
    context="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
    question="How long ago did dogs first become domesticated?",
    user_answer="around 20,000 years ago.",
    answer="Between 14,000 and 29,000 years ago."
)
print(json.dumps(output, indent=4))
