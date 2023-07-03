from .node import NodeConfig
from soffosai.core.services import AnswerScoringService, inspect_arguments
from soffosai.core.nodes.node import NodeConfig

class AnswerScoringNodeConfig(NodeConfig):
    '''
    Answer Scoring service configuration for Pipeline Use
    '''
    def __init__(self, context, question, user_answer, answer=None):
        service = AnswerScoringService
        source = inspect_arguments(self.__init__, context, question, user_answer, answer)
        super().__init__(service, source)
