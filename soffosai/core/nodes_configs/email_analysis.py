from .node import NodeConfig
from soffosai.core.services import EmailAnalysisService, inspect_arguments


class EmailAnalysisNodeConfig(NodeConfig):
    '''
    Email analysis configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__call__, text)
        service = EmailAnalysisService
        super().__init__(name, service, source)
