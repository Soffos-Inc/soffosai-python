from .node import Node
from soffosai.core.services import EmailAnalysisService, inspect_arguments


class EmailAnalysisNode(Node):
    '''
    Email analysis configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = EmailAnalysisService
        super().__init__(name, service, source)
