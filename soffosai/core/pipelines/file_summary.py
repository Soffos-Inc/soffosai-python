'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-30
Purpose: Define the standard Pipeline for converting and summarizing a file
-----------------------------------------------------
'''
from soffosai.core import Node, inspect_arguments
from soffosai.core.nodes import FileConverterNode, SummarizationNode
from soffosai.core.pipelines import Pipeline

class FileSummaryPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes a file, convert it to its text content then summarizes it.
    The output is a list containing the output object of file converter and summarization.
    '''
    def __init__(self, **kwargs) -> None:

        file_converter_node = FileConverterNode(
            name = "fileconverter",
            file = ("user_input", "file")
        )
        summarization_node = SummarizationNode(
            name = "summary",
            text = ("fileconverter"),
            sent_length = ("user_input", "sent_length")
        )

        nodes = [file_converter_node, summarization_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, file, sent_length):
        user_input = inspect_arguments(self.__call__, user, file, sent_length)
        return super().__call__(user_input)
