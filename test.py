import soffos
from soffos.core.services import QuestionAnsweringService, SoffosAIService
from soffos.common.constants import ServiceString

soffos.api_key = "Token a8fd8e5d-4909-4011-874c-724afc97d74c"
src = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    "message": "How can Soffos help me build amazing applications?",
    "document_text": "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]",
    "check ambiguity": True,
    "check_query_type": True,
    "generic_response": False,
    "meta": {
        "session_id": "69cb9520-885b-4f81-ae6c-79b8d63ff25c"
    }
}
# service = QuestionAnsweringService(
#     user = src.get("user"),
#     src=src
# )
# src = {
#   "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
#   "text": "I saw her duck",
#   "sentence_split": 3,
#   "sentence_overlap": True
# }
service = SoffosAIService(
    service= ServiceString.QUESTION_ANSWERING,
    user=src.get("user"),
    src=src
)

response = service.get_response()
print(response)
