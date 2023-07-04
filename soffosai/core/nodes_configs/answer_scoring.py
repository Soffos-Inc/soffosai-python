from .node import NodeConfig
from soffosai.core.services import AnswerScoringService, inspect_arguments


class AnswerScoringNodeConfig(NodeConfig):
    '''
    Answer Scoring service configuration for Pipeline Use
    '''
    def __init__(self, name:str, context:str, question:str, user_answer:str, answer:str=None):
        service = AnswerScoringService
        source = inspect_arguments(self.__init__, context, question, user_answer, answer)
        super().__init__(name, service, source)
