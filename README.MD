# Soffos.py
A Python software development kit for easy use of Soffos AI's APIs.

## API Keys
- Create an account at [Soffos platform](https://platform.soffos.ai) or [login](https://platform.soffos.ai/login).
- After loggin in, on the left panel, click [Projects](https://platform.soffos.ai/apps-list).
- Create a new project.
- Click on the key icon in the project you created and you will find the API Keys for that project.
  - An API key will automatically be provided for you on Project creation but you can still create more when your account is no longer on trial.
- Protect this API Key as it will incur charges.

## Installation
`pip install soffos`

## Syntax
- To set your api key:
```
import soffos
soffos.api_key = "YOUR_API_KEY"
```
put your api_key somewhere safe, off course. 

- These two imports are commonly used:
```
from soffos.core.services import SoffosAIService
from soffos.common.constants import ServiceString
```

- Specify your source:
```
src = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    "message": "What are the other terms for domestic dog?",
    "document_text": "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]",
}
```

- Create the SoffosAIService instance:
service = SoffosAIService(service=ServiceString.QUESTION_ANSWERING)

- You can also include the user in instantiating the SoffosAIService instance:
```
service = SoffosAIService(
    service=ServiceString.QUESTION_ANSWERING, 
    user="b5601df8-6af3-4c1a-9ded-b7df4c506eab"
)
```
if you are going to use this user on multiple service calls

- Call the service:
`response = service.get_response(src=src)`

- You can call the same service again for a different response by just changing the source:
```
src = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",`
    "message": "Some other question?",
    "document_text": "Some other context,
}
response = service.get_response(src=src)
```