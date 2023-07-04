from .node import NodeConfig
from soffosai.core.services import inspect_arguments, TranscriptCorrectionService


class TranscriptCorrectionNodeConfig(NodeConfig):
    '''
    Transcript Correction Service configuration for Pipeline Use
    '''
    def __init__(self, text:str):
        source = inspect_arguments(self.__call__, text)
        service = TranscriptCorrectionService
        super().__init__(service, source)
