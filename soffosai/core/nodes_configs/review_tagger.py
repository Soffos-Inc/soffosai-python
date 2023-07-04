from .node import NodeConfig
from soffosai.core.services import inspect_arguments, ReviewTaggerService


class ReviewTaggerNodeConfig(NodeConfig):
    '''
    Review Tagger Service configuration for Pipeline Use
    '''
    def __init__(self, text:str):
        source = inspect_arguments(self.__call__, text)
        service = ReviewTaggerService
        super().__init__(service, source)
