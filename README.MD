# Soffosai.py
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
`pip install soffosai`

## Syntax
- To set your api key:
```
import soffosai
soffosai.api_key = "YOUR_API_KEY"
```
Put your api_key somewhere safe, off course. 
If you included SOFFOSAI_API_KEY in your environment variables and specified your API key there, you don't need have this code: `soffosai.api_key = "YOUR_API_KEY"`

## SoffosAIService
The SoffosAIService class handles validation and execution of specified endpoint vs payload.
Here is the list of SoffosAIService Subclasses:
```
[
    "AmbiguityDetectionService",
    "AnswerScoringService",
    "ContradictionDetectionService",
    "DocumentsService",
    "DocumentsIngestService", 
    "DocumentsSearchService", 
    "DocumentsDeleteService", 
    "EmailAnalysisService",
    "FileConverterService",
    "LanguageDetectionService",
    "LetsDiscussService",
    "LogicalErrorDetectionService",
    "MicrolessonService",
    "NamedEntityRecognitionService",
    "ParaphraseService",
    "ProfanityService",
    "QuestionAndAnswerGenerationService",
    "QuestionAnsweringService",
    "ReviewTaggerService",
    "SentimentAnalysisService",
    "SimplifyService",
    "SummarizationService",
    "TableGeneratorService",
    "TagGenerationService",
    "TranscriptCorrectionService",
]

```
- Instantiate the SoffosAIService that you need:
```
from soffosai import *

service = SummarizationService()
```

- Call the service and print the output:
```
output = service(
    user = "client_id",
    text = "Ludwig van Beethoven (baptised 17 December 1770 – 26 March 1827) was a German composer and pianist. ... After some months of bedridden illness, he died in 1827. Beethoven's works remain mainstays of the classical music repertoire.",
    sent_length=2
)
print(json.dumps(output, indent=4))
```

## Samples
Sample code for each service can be found on [tests/services](https://github.com/Soffos-Inc/soffos_ai/tree/master/tests/services)


## Pipeline
A Pipeline is a collection of services working together to generate a required output given a set of inputs.

### NodeConfig
- To easily create a pipeline, you need to create NodeConfigs (node configuration).  A NodeConfig is a service configuration that will tell the Pipeline what the service is to be used and where in the pipe would it get its input:
```
import json
from soffosai.core import NodeConfig
from soffosai.common.constants import ServiceString

src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix",
    "question": "who is Neo?"
}

file_converter_node = NodeConfig(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file")
    }
)
```

### Use the NodeConfigs as input of the Pipeline
```
import json
from soffosai.core import Pipeline
from soffosai.core import NodeConfig
from soffosai.common.constants import ServiceString


src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix",
    "question": "who is Neo?"
}

file_converter_node = NodeConfig(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file"), # get the value for "file" field from user_input (0) with the key "file"
        "normalize": 0 # meaning the pipeline will always 0 as the value of this field
    }
)

document_ingest_node = NodeConfig(
    service=ServiceString.DOCUMENTS_INGEST,
    source={
        "name": (0, "name"), # get the value for "name" field from user_input (0) with the key "name"
        "text": (1, "text")  # get the value for "text" field from 1st stage (1) output with the key "text"
    }
)

question_answering_node = NodeConfig(
    service=ServiceString.QUESTION_ANSWERING,
    source={
        "document_ids": (2, "document_id"), # get the value for "document_ids" field from 2nd stage (2) output with the key "document_ids"
        "question": (0, "question")
    }
)

# This is one way to define your pipeline
my_pipe = Pipeline(
    stages = [file_converter_node, document_ingest_node, question_answering_node]
)
output = my_pipe.run(user_input=src)
print(json.dumps(output, indent=4))

# But there is a better way
```

### Better way to define your own Custom Pipeline
As an example, this is the a custom pipeline included in the package as one of the standard Pipelines:
```
'''
This is a better way to create your custom Pipeline.
The __call__ method gives you the power to put the arguments and makes calling your Pipeline so much easier
'''

from soffosai import ServiceString
from soffosai.core import NodeConfig, Pipeline, inspect_arguments


class FileIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then saves it to Soffos db.
    the output is a list containing the output object of file converter and document ingest
    '''

    # override the constructor of the Pipeline
    def __init__(self, **kwargs) -> None:

        # define your nodes
        file_converter_node = NodeConfig(
            service=ServiceString.FILE_CONVERTER,
            source = {
                "file": (0, "file"),
                "normalize": 0
            }
        )

        document_ingest_node = NodeConfig(
            service = ServiceString.DOCUMENTS_INGEST,
            source = {
                "text": (1, "text"),
                "name": (0, "name")
            }
        )

        # define the stages
        stages = [file_converter_node, document_ingest_node]
        use_defaults = False

        # supply the stages to the superclass constructor
        super().__init__(stages=stages, use_defaults=use_defaults, **kwargs)


    # override the callable method
    def __call__(self, user, file, name): # define what your pipeline needs, arguments instead of dictionary
        user_input = inspect_arguments(self.__call__, user, file, name) # convert the args to dict
        return super().__call__(user_input)

    '''
    The inspect_arguments helper function takes the function name as the first argument then
    the rest of the arguments of the same function. Please put them in order you assign them 
    to the function itself. As you can observe, __call__ and inspect_arguments both have the 
    arguments listed as user, file, name.
    '''
```

### Use Defaults
The Pipeline has a use_defaults argument that defaults to False. If set to True:
stages will take input from the previous stages' output of the same field name prioritizing the latest stage's output. If the previous stages does not have it, it will take from the pipeline's user_input.  Also, the stages will only be supplied with the required fields + default of the require_one_of_choice fields.  

Use this feature if you are familiar with the input and output keys of the services your
are cascading.  This will make the definition of your pipeline shorter:
```
import json
from soffosai import ServiceString
from soffosai.core import NodeConfig, Pipeline, inspect_arguments


class FileIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then saves it to Soffos db.
    the output is a list containing the output object of file converter and document ingest
    '''

    # override the constructor of the Pipeline
    def __init__(self, **kwargs) -> None:

        # define your nodes even without the sources
        file_converter_node = NodeConfig(service=ServiceString.FILE_CONVERTER)
        document_ingest_node = NodeConfig(service = ServiceString.DOCUMENTS_INGEST)

        # define the stages
        stages = [file_converter_node, document_ingest_node]
        use_defaults = True # dynamically create the source configuration of the Nodes
        super().__init__(stages=stages, use_defaults=use_defaults, **kwargs)


    # make sure you know the required input fields
    def __call__(self, user, file, name): # define what your pipeline needs, arguments instead of dictionary
        user_input = inspect_arguments(self.__call__, user, file, name) # convert the args to dict
        return super().__call__(user_input)
```


### Where to get the required fields for Services
To know the required fields of each SoffosAIService, they are defined in:
```soffosai.common.serviceio_fields``` or [visit the api documentation](https://platform.soffos.ai/playground/docs#)
