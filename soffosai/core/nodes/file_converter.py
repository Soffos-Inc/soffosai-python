from soffosai.core.services import FileConverterService, SummarizationService, inspect_arguments
from .node import Node


class FileConverterNode(Node):
    '''
    File Converter Node for Pipeline Use
    '''
    def __init__(self, name:str, file) -> None:
        service = FileConverterService
        source = inspect_arguments(self.__init__, name, file)
        super().__init__(name, service, source)
