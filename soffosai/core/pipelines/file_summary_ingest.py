'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-30
Purpose: Define the standard Pipeline for converting, summarizing then ingesting a file
-----------------------------------------------------
'''
from soffosai import ServiceString
from soffosai.core import Node, inspect_arguments
from soffosai.core.pipelines import Pipeline

class FileSummaryIngestPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content, summarizes it
    then saves it to Soffos db.
    The output is a list containing the output object of file converter, summarization and document ingest
    '''
    def __init__(self, **kwargs) -> None:
        file_converter_node = Node(
            service=ServiceString.FILE_CONVERTER,
            source = {
                "file": (0, "file"),
            }
        )

        summarization_node = Node(
            service=ServiceString.SUMMARIZATION,
            source = {
                "text": (1, "text"),
                "sent_length": (0, "sent_length")
            }
        )

        document_ingest_node = Node(
            service = ServiceString.DOCUMENTS_INGEST,
            source = {
                "text": (2, "summary"),
                "name": (0, "name")
            }
        )

        stages = [file_converter_node, summarization_node, document_ingest_node]
        use_defaults = False
        super().__init__(stages=stages, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, file, sent_length, name):
        user_input = inspect_arguments(self.__call__, user, file, sent_length, name)
        return super().__call__(user_input)
