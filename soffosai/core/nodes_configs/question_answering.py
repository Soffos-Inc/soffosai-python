from .node import NodeConfig
from soffosai.core.services import inspect_arguments, QuestionAnsweringService


class QuestionAnsweringNodeConfig(NodeConfig):
    '''
    Question Answering Service configuration for Pipeline Use
    '''
    def __init__(self, question:str, document_text:str=None, document_ids:list=None, 
        check_ambiguity:bool=True, check_query_type:bool=True, generic_response:bool=False, meta:dict=None):

        source = inspect_arguments(self.__call__, question, document_text, document_ids, 
        check_ambiguity, check_query_type, generic_response, meta)
        source['message'] = question

        service = QuestionAnsweringService
        super().__init__(service, source)
