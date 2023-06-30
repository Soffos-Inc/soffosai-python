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
    