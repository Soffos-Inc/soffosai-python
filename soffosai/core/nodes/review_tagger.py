from .node import Node
from soffosai.core.services import inspect_arguments, ReviewTaggerService


class ReviewTaggerNode(Node):
    '''
    Review Tagger Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = ReviewTaggerService
        super().__init__(name, service, source)
