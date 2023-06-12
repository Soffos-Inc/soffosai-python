import soffos
from soffos.nodes.node import ServiceNode
from soffos.core import services
from soffos.client import SoffosAiResponse


soffos.api_key = "c7ddde25-a5a1-4cfe-9cf1-4c5c6005525f"

src = {
    "user": "test_user",
    "message": "What are the other term for dogs",
    "document_text": "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]"
}

node = ServiceNode(
    service = services.QuestionAnsweringService,
    source = src
)

response = node.run()

print(response)
