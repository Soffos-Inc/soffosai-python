# Welcome to the Soffos Platform SDK
The Soffos Generative AI platform is a revolutionary solution that empowers Edtech developers to create or enhance custom AI applications for learning and development, without the need for special AI skills. Additionally, the Soffos Platform provides generative AI tools that instructional designers can use directly to create training materials.

# Product Designers and Developers can create simple to complex apps with our SDK
The Soffos Software Development Kit (SDK) and RESTful APIs are low-code tools that help L&D teams accelerate their AI adoption without the need for AI expertise, making the creation of generative AI solutions for L&D easier and faster.

The Soffos SDK is available for Python and JavaScript developers. It includes a pipeline to sequence and deploy multiple modules, while providing asynchronous events to monitor NLP and generative AI operations for truly engaging user experiences. The Soffos platform offers a selection of premier large language models and provides the convenience of automatic failover to alternative models should your preferred choice become unavailable.

At Soffos, our mission is clear – to make the creation of learning materials easier and more efficient using generative AI.

Visit the [Soffos Platform](https://www.soffos.ai) and start building your first generative AI application today!

Join our Discord channel: [SoffosAI](https://discord.gg/Q2yTEuFG2B)

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
    "AnswerScoringService",
    "AssessmentGeneratorService"
    "AudioConverterService",
    "ChatBotCreateService",
    "ChatBotDeleteUserSessionsService",
    "ChatBotGetUserSessionsService",
    "ChatBotsDeleteService",
    "ChatBotService",
    "ChatBotsGetService",
    "DiscussQueryService",
    "DiscussCountService",
    "DiscussCreateService",
    "DiscussDeleteService",
    "DocumentsCountService",
    "DocumentsIngestService", 
    "DocumentsSearchService", 
    "DocumentsDeleteService", 
    "EmailAnalysisService",
    "FileConverterService",
    "ImageAnalysisService",
    "ImageGenerationService",
    "MicrolessonService",
    "MultipleChoiceQnAGeneratorService",
    "NERService",
    "NaturalSQLGenerationService",
    "SimplifyService",
    "SummarizationService",
    "TableGeneratorService",
    "TagService",
    "TableDeleteService",
    "TableGetService",
    "TableIngestService",
    "TranscriptCorrectionService",
    "TranslationService",
    "WebsiteConverterService",
]

```
- Instantiate the SoffosAIService that you need:
```
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"

service = SoffosAIServices.SummarizationService()
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

### Samples
- Sample code for each service can be found on [samples/services](https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services)
- Google Colab notebooks:
    - [Document ingestion and question-answering example](https://colab.research.google.com/drive/18BWXlPjLWaFzvzqU6TP_cMAGubQOWxzP?usp=sharing)
    - [Question generation and answer scoring.](https://colab.research.google.com/drive/1aY9k_GzPFu99Dr-EELeBPFOc3fayUytR?usp=sharing)

### Where to get the required fields for Services
To know the required fields of each SoffosAIService, they are defined in:
```soffosai.common.serviceio_fields``` or [visit the api documentation](https://platform.soffos.ai/playground/docs#)


## Pipeline
A Pipeline is a collection of services working together to generate a required output given a set of inputs.

### set_input_configs
- To easily create a pipeline, you need to call set_input_configs of a SoffosAIService.  It will then be configured for Pipeline use. It tells the Pipeline what the service is to be used and where in the pipeline would it get its input. You can define a constant as an input of a set_input_configs or create an InputConfig to define where to get the input of this Service.

#### InputConfig
- To pre-define an input for a Service that depends on the output of other Services, you should create an InputConfig:
```
from soffosai import InputConfig
```
- It takes 3 arguments: source, file, pre_process
    source: The name of the Servie or Pipeline from where the input of the current Service should be taken from.
    field: The name of the output field of the "source".
    pre_process (optional): A function to pre-processes the data from source[field] before supplying it as the Service's argument.

#### Service preparation for Pipeline use declaration
```
import json
from soffosai import FileConverterService, InputConfig

file_input_config = InputConfig(source="user_input", field="file")# this argument will take the value from user_input['file]

file_converter = FileConverterService().set_input_configs( # this service uses the FileConverterService
    name = "fileconverter", # for reference of the entire pipeline, this service is named "fileconverter"
    file = file_input_config
)
```

### Use the Service as input of the Pipeline
```
import json
from soffosai.core.pipelines import Pipeline
from soffosai import FileConverterService, DocumentsIngestService, QuestionAnsweringService, InputConfig

# a helper function to get the filename provided the file is in the same directory
def get_filename(full_file_name:str):
    return full_file_name.split(".")[0]


# a helper function that puts the document_id inside a list. Useful when the source service's output is
# document_id and the current service needs document_ids
def put_docid_inside_list(doc_id):
    return [doc_id]


# initialize the generic Pipeling
my_pipe = Pipeline(
    # define your services in order of execution
    services = [
        FileConverterService().set_input_configs(
            name="fileconv", # This service will be referenced by other services as "fileconv"
            file = InputConfig("user_input", "file") #  get user_input['file']
        ), 
        DocumentsIngestService().set_input_configs(
            name = 'ingest', 
            document_name=InputConfig("user_input", "file", get_filename)# this argument needs the 
                    #return value of get_filename(user_input['file'])
            text=InputConfig("fileconv", "text") # this service needs its text argument to come from fileconv output field 'text'.
        ),
        QuestionAnsweringService().set_input_configs(
            name="qa",
            question=InputConfig("user_input", "question"), 
            document_ids=InputConfig("ingest", "document_id", "put_docid_inside_list")# this argument needs the return value of put_docid_inside_list(<output of "ingest" service with key "document_id">)
        )
    ]
)

src = {
    "user": "client_id", 
    "file": "matrix.pdf",
    "question": "who is Neo?"
}
output = my_pipe.run(user_input=src)
print(json.dumps(output, indent=4))


# But there is a better way
```

### More advanced and conigurable way to create a Pipeline
As an example, this is the a custom pipeline included in the package as one of the standard Pipelines:
```
'''
This is a better way to create your custom Pipeline.
The __call__ method gives you the power to put the arguments and makes calling your Pipeline so much easier
'''

import json
from soffosai import FileConverterService, SummarizationService, DocumentsIngestService, InputConfig
from soffosai.core.pipelines import SoffosPipeline

class FileSummaryIngestPipeline(SoffosPipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content, summarizes it
    then saves it to Soffos db.
    The output is a list containing the output object of file converter, summarization and document ingest
    '''
    def __init__(self, **kwargs) -> None:

        file_converter = FileConverterService().set_input_configs(
            name = "fileconverter",
            file = InputConfig("user_input", "file")
        )
        summarization = SummarizationService().set_input_configs(
            name = "summary",
            text = InputConfig("fileconverter", "text"),
            sent_length = InputConfig("user_input", "sent_length")
        )
        document_ingest = DocumentsIngestService().set_input_configs(
            name = "ingest",
            text = InputConfig("summary", "summary"),
            document_name = InputConfig("user_input", "file")
        )

        services = [file_converter, summarization, document_ingest]
        use_defaults = False
        super().__init__(services=services, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, file, sent_length):
        return super().__call__(user=user, file=file, sent_length=sent_length)


# initialize the Pipeline
my_pipe = FileSummaryIngestPipeline()
# call it
output = my_pipe(
    user = "client_id",
    file = "matrix.pdf",
    sent_length = 5
)
print(json.dumps(output, indent=4))

```

### Helper functions
You can use helper functions if you need the value of an element to be processed before it is used.
```
def put_docid_inside_list(doc_id):
    return [doc_id]

QuestionAnsweringService.set_input_config(
    name="qa",
    question=InputConfig("user_input", "question"), 
    document_ids=InputConfig("ingest", "document_id", put_docid_inside_list)# this argument needs the return 
    # value of put_docid_inside_list(<output of ingest service with key 'document_id'>)
)
```
When you use a helper function, the field will not be checked for datatype.  The fields will still be checked if complete.

### Use Defaults
The Pipeline has a use_defaults argument that defaults to False. If set to True:
services will take input from the previous services' output of the same field name prioritizing the latest service's output. If the previous services does not have it, it will take from the pipeline's user_input.  Also, the services will only be supplied with the required fields + default of the require_one_of_choice fields.  

Use this feature if you are familiar with the input and output keys of the services your
are cascading.  This will make the definition of your pipeline shorter:
```
import json
from soffosai import ServiceString
from soffosai import SoffosAIService, Pipeline, inspect_arguments


class FileIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then saves it to Soffos db.
    the output is a list containing the output object of file converter and document ingest
    '''

    # override the constructor of the Pipeline
    def __init__(self, **kwargs) -> None:

        # define your services even without the sources
        file_converter_service = SoffosAIService(service=ServiceString.FILE_CONVERTER)
        document_ingest_service = SoffosAIService(service = ServiceString.DOCUMENTS_INGEST)

        # arrange the services according to execution
        services = [file_converter_service, document_ingest_service]
        use_defaults = True # dynamically create the source configuration of the SoffosAIServices
        super().__init__(services=services, use_defaults=use_defaults, **kwargs)


    # make sure you know the required input fields
    def __call__(self, user, file, name): # define what your pipeline needs, arguments instead of dictionary
        user_input = inspect_arguments(self.__call__, user, file, name) # convert the args to dict
        return super().__call__(user_input)
```
### Pipelines Examples
You can check how the Pipelines are created at [samples/pipelines](https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/pipelines) and in [pipelines](https://github.com/Soffos-Inc/soffosai-python/tree/master/soffosai/core/pipelines)


### Pipeline as Service Inside a Pipeline
Pipelines can be Service inside a Pipeline.
```
from soffosai import FileConverterService, SummarizationService, DocumentsIngestService, InputConfig
from soffosai import QuestionAnsweringService
from soffosai.core.pipelines import SoffosPipeline

# Define the Pipeline to be used as a Service

class FileSummaryIngestPipeline(SoffosPipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content, summarizes it
    then saves it to Soffos db.
    The output is a list containing the output object of file converter, summarization and document ingest
    '''
    def __init__(self, **kwargs) -> None:

        file_converter = FileConverterService().set_input_configs(
            name = "fileconverter",
            file = InputConfig("user_input", "file")
        )
        summarization = SummarizationService().set_input_configs(
            name = "summary",
            text = InputConfig("fileconverter", "text"),
            sent_length = InputConfig("user_input", "sent_length")
        )
        document_ingest = DocumentsIngestService().set_input_configs(
            name = "ingest",
            text = InputConfig("summary", "summary"),
            document_name = InputConfig("user_input", "file")
        )

        services = [file_converter, summarization, document_ingest]
        use_defaults = False
        super().__init__(services=services, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, file, sent_length):
        return super().__call__(user=user, file=file, sent_length=sent_length)


def get_doc_ids(document_id):
    return [document_id]

class PipeInPipeSample(Pipeline):
    def __init__(self, **kwargs) -> None:
        
        the_pipe = FileSummaryIngestPipeline(name="summary_id")
        qa = QuestionAnsweringService.set_input_config(
            name='qa',
            question=InputConfig("user_input", "question"),
            document_ids=InputConfig(
                source = "summary_id",
                field = "document_id",
                pre_process = get_doc_ids
            )
        )
        services = [the_pipe, qa]
        super().__init__(services, **kwargs)


    def __call__(self, user, file, sent_length, question):
        return super().__call__(user=user, file=file, sent_length=sent_length, question=question)
```

Copyright (c)2023 - Soffos.ai - All rights reserved