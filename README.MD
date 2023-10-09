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

### Samples
Sample code for each service can be found on [samples/services](https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services)

### Where to get the required fields for Services
To know the required fields of each SoffosAIService, they are defined in:
```soffosai.common.serviceio_fields``` or [visit the api documentation](https://platform.soffos.ai/playground/docs#)


## Pipeline
A Pipeline is a collection of services working together to generate a required output given a set of inputs.

### Node
- To easily create a pipeline, you need to create Nodes.  A Node is a service configured for Pipeline use. It tells the Pipeline what the service is to be used and where in the pipeline would it get its input. You can define a constant as an input of a Node or create an InputConfig to define where to get the input of this Node.
#### InputConfig
- To define an input for a Node that depends on the output of other Nodes, you should create an InputConfig:
```
from soffosai.core.nodes import InputConfig
```
- It takes 3 arguments: source, file, pre_process
    source: The name of the Node or Pipeline from where the input of the current Node should be taken from.
    field: The name of the output field of the "source".
    pre_process (optional): A function to pre-processes the data from source[field] before supplying it as the Node's argument.

#### Node declaration
```
import json
from soffosai.core.nodes import FileConverterNode, InputConfig

file_input_config = InputConfig(source="user_input", field="file")# this argument will take the value from user_input['file]

file_converter_node = FileConverterNode( # this node uses the FileConverterService
    name = "fileconverter", # for reference of the entire pipeline, this node is named "fileconverter"
    file = file_input_config
)
```

### Use the Node as input of the Pipeline
```
import json
from soffosai.core.pipelines import Pipeline
from soffosai.core.nodes import FileConverterNode, DocumentsIngestNode, QuestionAnsweringNode, InputConfig

# a helper function to get the filename provided the file is in the same directory
def get_filename(full_file_name:str):
    return full_file_name.split(".")[0]


# a helper function that puts the document_id inside a list. Useful when the source node's output is
# document_id and the current node needs document_ids
def put_docid_inside_list(doc_id):
    return [doc_id]


# initialize the generic Pipeling
my_pipe = Pipeline(
    # define your nodes in order of execution
    nodes = [
        FileConverterNode(
            name="fileconv", # This node will be referenced by other nodes as "fileconv"
            file = InputConfig("user_input", "file") #  get user_input['file']
        ), 
        DocumentsIngestNode(
            name = 'ingest', 
            document_name=InputConfig("user_input", "file", get_filename)# this argument needs the 
                    #return value of get_filename(user_input['file'])
            text=InputConfig("fileconv", "text") # this node needs its text argument to come from fileconv output field 'text'.
        ),
        QuestionAnsweringNode(
            name="qa",
            question=InputConfig("user_input", "question"), 
            document_ids=InputConfig("ingest", "document_id", "put_docid_inside_list")# this argument needs the return value of put_docid_inside_list(<output of "ingest" node with key "document_id">)
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
from soffosai.core import inspect_arguments
from soffosai.core.nodes import FileConverterNode, SummarizationNode, DocumentsIngestNode, InputConfig
from soffosai.core.pipelines import Pipeline

class FileSummaryIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content, summarizes it
    then saves it to Soffos db.
    The output is a list containing the output object of file converter, summarization and document ingest
    '''
    # override the constructor of the Pipeline
    def __init__(self, **kwargs) -> None:

        # define your nodes
        file_converter_node = FileConverterNode(
            name = "fileconverter",
            file = InputConfig("user_input", "file"()
        )
        summarization_node = SummarizationNode(
            name = "summary",
            text = InputConfig("fileconverter", "text"),
            sent_length = InputConfig("user_input", "sent_length")
        )
        document_ingest_node = DocumentsIngestNode(
            name = "ingest",
            text = InputConfig("summary", "summary"),
            document_name = InputConfig("user_input", "file")
        )

        # define the list of nodes in order of execution
        nodes = [file_converter_node, summarization_node, document_ingest_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    # override the __call__ method
    def __call__(self, user, file, sent_length): # set the user_input keys as arguments here
        user_input = inspect_arguments(self.__call__, user, file, sent_length)# convert the args to dict
        return super().__call__(user_input)

# initialize the Pipeline
my_pipe = FileSummaryIngestPipeline()
# call it
output = my_pipe(
    user = "client_id",
    file = "matrix.pdf",
    sent_length = 5
)
print(json.dumps(output, indent=4))

'''
    The inspect_arguments helper function takes the function name as the first argument then
    the rest of the arguments of the same function. Please put them in order you assign them 
    to the function itself. As you can observe, __call__ and inspect_arguments both have the 
    arguments listed as user, file, name.
'''
```

### Helper functions
You can use helper functions if you need the value of an element to be processed before it is used.
```
def put_docid_inside_list(doc_id):
    return [doc_id]

QuestionAnsweringNode(
    name="qa",
    question=InputConfig("user_input", "question"), 
    document_ids=InputConfig("ingest", "document_id", put_docid_inside_list)# this argument needs the return value of put_docid_inside_list(<output of ingest node with key 'document_id'>)
)
```
When you use a helper function, the field will not be checked for datatype.  The fields will still be checked if complete.

### Use Defaults
The Pipeline has a use_defaults argument that defaults to False. If set to True:
nodes will take input from the previous nodes' output of the same field name prioritizing the latest node's output. If the previous nodes does not have it, it will take from the pipeline's user_input.  Also, the nodes will only be supplied with the required fields + default of the require_one_of_choice fields.  

Use this feature if you are familiar with the input and output keys of the services your
are cascading.  This will make the definition of your pipeline shorter:
```
import json
from soffosai import ServiceString
from soffosai.core import Node, Pipeline, inspect_arguments


class FileIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then saves it to Soffos db.
    the output is a list containing the output object of file converter and document ingest
    '''

    # override the constructor of the Pipeline
    def __init__(self, **kwargs) -> None:

        # define your nodes even without the sources
        file_converter_node = Node(service=ServiceString.FILE_CONVERTER)
        document_ingest_node = Node(service = ServiceString.DOCUMENTS_INGEST)

        # arrange the nodes according to execution
        nodes = [file_converter_node, document_ingest_node]
        use_defaults = True # dynamically create the source configuration of the Nodes
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    # make sure you know the required input fields
    def __call__(self, user, file, name): # define what your pipeline needs, arguments instead of dictionary
        user_input = inspect_arguments(self.__call__, user, file, name) # convert the args to dict
        return super().__call__(user_input)
```
### Pipelines Examples
You can check how the Pipelines are created at [samples/pipelines](https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/pipelines) and in [pipelines](https://github.com/Soffos-Inc/soffosai-python/tree/master/soffosai/core/pipelines)


### Pipeline as Node Inside a Pipeline
Pipelines can be Node inside a Pipeline.
```
# Define the Pipeline to be used as a Node
class FileSummaryIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content, summarizes it
    then saves it to Soffos db.
    The output is a list containing the output object of file converter, summarization and document ingest
    '''
    # override the constructor of the Pipeline
    def __init__(self, name=None, **kwargs) -> None:

        # define your nodes
        file_converter_node = FileConverterNode(
            name = "fileconverter",
            file = InputConfig("user_input", "file")
        )
        summarization_node = SummarizationNode(
            name = "summary_node",
            text = InputConfig("fileconverter", "text"),
            sent_length = InputConfig("user_input", "sent_length")
        )
        document_ingest_node = DocumentsIngestNode(
            name = "ingest",
            text = InputConfig("summary_node", "summary"),
            document_name = InputConfig("user_input", "file")
        )

        # define the list of nodes in order of execution
        nodes = [file_converter_node, summarization_node, document_ingest_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, name=name,**kwargs)


    # override the callable method and expose the output
    def __call__(self, user, file, sent_length): # set the user_input keys as arguments here
        user_input = inspect_arguments(self.__call__, user, file, sent_length)# convert the args to dict
        response = super().__call__(user_input)



def get_doc_ids(document_id):
    return [document_id]

class PipeInPipeSample(Pipeline):
    def __init__(self, **kwargs) -> None:
        
        the_pipe = FileSummaryIngestPipeline(name="summary_id")
        qa = QuestionAnsweringNode(
            name='qa',
            question=InputConfig("user_input", "question"),
            document_ids=InputConfig(
                source = "summary_id",
                field = "document_id",
                pre_process = get_doc_ids
            )
        )
        nodes = [the_pipe, qa]
        super().__init__(nodes, **kwargs)


    def __call__(self, user, file, sent_length, question):
        user_input = inspect_arguments(self.__call__, user, file, sent_length, question)
        return super().__call__(user_input)
```

Copyright (c)2023 - Soffos.ai - All rights reserved