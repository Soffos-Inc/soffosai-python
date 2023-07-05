'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-30
Purpose: Define the standard Pipeline for converting, summarizing an ingested document
-----------------------------------------------------
'''
from soffosai import ServiceString, DocumentsSearchService
from soffosai.core import Node, inspect_arguments
from soffosai.core.pipelines import Pipeline

class DocumentSummaryPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes document_ids, then summarizes the content.
    The output is a list containing the output object of file converter and summarization.
    '''
    def __init__(self, **kwargs) -> None:
        document_search_node = Node(
            service=DocumentsSearchService,
            source = {
                "document_ids": (0, "document_ids")
            }
        )

        summarization_node = Node(
            service=ServiceString.SUMMARIZATION,
            source = {
                "text": (1, "text"),
                "sent_length": (0, "sent_length")
            }
        )

        stages = [document_search_node, summarization_node]
        use_defaults = False
        super().__init__(stages=stages, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, document_ids, sent_length):
        user_input = inspect_arguments(self.__call__, user, document_ids, sent_length)
        return super().__call__(user_input)
