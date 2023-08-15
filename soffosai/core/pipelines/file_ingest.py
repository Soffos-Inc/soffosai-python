'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-29
Purpose: Define the standard Pipeline for converting then ingesting a file
-----------------------------------------------------
'''
from soffosai.core import inspect_arguments
from soffosai.core.nodes import FileConverterNode, DocumentsIngestNode
from soffosai.core.pipelines import Pipeline

class FileIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then saves it to Soffos db.
    the output is a list containing the output object of file converter and document ingest
    '''
    def __init__(self, **kwargs) -> None:


        file_converter_node = FileConverterNode(
            name = "fileconverter",
            file = {"source": "user_input", "field": "file"}
        )
        document_ingest_node = DocumentsIngestNode(
            name = "ingest",
            document_name = {"source": "user_input", "field": "file"},
            text = {"source": "fileconverter", "field": "text"}
        )

        nodes = [file_converter_node, document_ingest_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, file):
        user_input = inspect_arguments(self.__call__, user, file)
        return super().__call__(user_input)
