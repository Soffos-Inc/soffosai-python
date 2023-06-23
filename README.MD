# Soffos.py
A Python software development kit for using Soffos AI's APIs.

## API Keys
- Create an account at [Soffos platform](https://platform.soffos.ai) or [login](https://platform.soffos.ai/login).
- After loggin in, on the left panel, click [Projects](https://platform.soffos.ai/apps-list).
- Create a new project.
- Click on the key icon in the project you created and you will find the API Keys for that project.
  - An API key will automatically be provided for you on Project creation but you can still create more when your account is no longer on trial.
- Protect this API Key as it will incur charges.
- You can also save your API Key into your environment variables with variable name = SOFFOSAI_API_KEY

## Installation
`pip install soffos`

## Syntax
- To set your api key:
```
import soffos
soffos.api_key = "YOUR_API_KEY"
```
Put your api_key somewhere safe, off course. 
If you included SOFFOSAI_API_KEY in your environment variables and specified your API key there, you don't need have this code: `soffos.api_key = "YOUR_API_KEY"`

- These two imports are commonly used:
```
from soffos.core.services import SoffosAIService
from soffos.common.constants import ServiceString
```

- Specify your payload:
```
payload = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    "message": "What are the other terms for domestic dog?",
    "document_text": "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]",
}
```

## SoffosAIService
The SoffosAIService class handles validation and execution of specified endpoint vs payload
- Create the SoffosAIService instance:
```
service = SoffosAIService(service=ServiceString.QUESTION_ANSWERING)
```

- Call the service:
```
response = service(payload=payload)
print(response)
```

- You can call the same service again for a different response by just changing the source:
```
src = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",`
    "message": "Some other question?",
    "document_text": "Some other context,
}
response = service.get_response(src=src)
print(response)
```

## Nodes
Nodes are service wrappers.  It prepares the SoffosAIService for Pipeline Use.
You can also Use Nodes like a Service.
When using Nodes, you can specify which node number you want to get your data:
```
from soffos.core.nodes import ServiceNode
from soffos.common.constants import ServiceString

src = {
    "user": "test_user",
    "message": "What are the other term for dogs",
    "document_text": "The dog or domestic dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8] The dog was the first species to be domesticated,[9][8] by hunter–gatherers over 15,000 years ago,[7] before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]"
}

node = ServiceNode(
    service = ServiceString.QUESTION_ANSWERING,
)

response = node.run(src)
print(response)
```

If you need to specify the Node number, the value of the source keys should be a tuple:
```
src = {
    "user": (0, "user"),
    "message": (1, "text"),
    "document_text": (2, "context")
}
```
In this source, you are specifying to take the "user" value from the source dictionary with the key "user". Then the "message" value from the output of the 1st Node with the key "text". Lastly take the output of the second node with key "context" and assign this as the value of this source's "document_text" item. But this notation of the source is just for the Pipeline. It will not be accepted for running a single node.

## Further Documentation
For complete documentation of source and response keys: [soffos.ai documentation](https://platform.soffos.ai/playground/docs#/). In here you will find all available services and their required arguments.

For the File Ingest Service though, you only need to specify the directory of the file:
```
src = {
    "user": "sample_user",
    "file": "location/of/the/file.pdf"
}
```

## SoffosPipeline
By using SoffosPipeline class, you get very easy sequenced call to multiple Soffos Services. Let us explain by example (explanations in the comments):
```
import soffos
from soffos.core.pipeline import SoffosPipeline
from soffos.core.nodes import ServiceNode
from soffos.common.constants import ServiceString

# authentication
soffos.api_key = "<your api key>"

# the pipeline's source. This is referred to as info[0] in the pipeline
src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix"
}

# create a node instance that uses the file converter service.
# accepts a file and extracts information.
file_converter_node = ServiceNode(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file") # this means: get from source (info[0]), the key "file"
    }
)

# create a node instance that uses the documents ingest service.
# uploads the context to our db for faster performance and for future use.
document_ingest_node = ServiceNode(
    service=ServiceString.DOCUMENTS_INGEST,
    source={
        "name": (0, "name"), # get from source (info[0]), with key = "name"
        "text": (1, "text") # get from output of first node (info[1]), with key = "text"
    }
)

# create a node instance that uses the question answering service.
# takes document_ids or text (not both), a message (a question) and returns an answer based on the docs.
question_answering_node = ServiceNode(
    service=ServiceString.QUESTION_ANSWERING,
    source={
        "document_ids": (2, "document_id"), # output of second node (info[2]), key = "document_id"
        "message": "Who is Neo?" # use this actual value
    }
)

# create a SoffosPipeline instance
# runs the nodes in sequence
my_pipe = SoffosPipeline(
    stages = [file_converter_node, document_ingest_node, question_answering_node],
    user = 'franco',
    source = src
)

# Run the pipeline and print the result.
# The result will be a list of infos. info[0] is the source, info[1] is the output of first node,
# info[2] is the output of the second node, etc...
print(my_pipe.run())
```