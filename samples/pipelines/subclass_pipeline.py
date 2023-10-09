'''
This is a better way to create your custom Pipeline.
The __call__ method gives you the power to put the arguments and makes calling your Pipeline so much easier
'''
import json
from soffosai.core import inspect_arguments
from soffosai.core.nodes import FileConverterNode, SummarizationNode, DocumentsIngestNode
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
            file = {"source": "user_input", "field": "file"}
        )
        summarization_node = SummarizationNode(
            name = "summary",
            text = {"source": "fileconverter", "field": "text"},
            sent_length = {"source": "user_input", "field": "sent_length"}
        )
        document_ingest_node = DocumentsIngestNode(
            name = "ingest",
            text = {"source": "summary", "field": "summary"},
            document_name = {"source": "user_input", "field": "file"}
        )

        # define the list of nodes in order of execution
        nodes = [file_converter_node, summarization_node, document_ingest_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    # override the callable method
    def __call__(self, user, file, sent_length):
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