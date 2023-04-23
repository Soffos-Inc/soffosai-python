'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''
import uuid
from soffos.common.constants import SERVICES_LIST, Services
from soffos.core.services import *
from .ai_response import SoffosAiResponse


SERVICE_CLASS_MAP = {
    Services.QUESTION_ANSWERING: QuestionAnsweringService,
    Services.FILE_CONVERTER: FileConverterService,
    Services.AMBIGUITY_DETECTION: AmbiguityDetectionService,
    Services.ANSWER_SCORING: AnswerScoringService,
    Services.CONTRADICTION_DETECTION: ContradictionDetectionService
}


def is_valid_uuid(uuid_string):
    try:
        uuid_obj = uuid.UUID(uuid_string)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_string


class Client:
    '''
    Not finished yet -- Just warming up
    ------------------------------------
    handles Soffos API http requests
    '''

    def __init__(self, apikey, user=None) -> dict:

        self._apikey = apikey
        self.headers = {
            "x-api-key": apikey,
            "content-type": "application/json"
        }
        self._src = None
        self._question = None
        self._concern = None
        self._answer = None
        self._tags = None
        self._service = None
        self._output_key = None
        self._user = user
        self._normalize = False
        self._sentence_split = 4
        self._sentence_overlap = False
        self._user_answer = None
        self._document_ids = None
        self._tagged_elements = None
        
        # read-only attributes
    
    @property
    def document_ids(self) -> list:
        '''
        The document id of the ingested document to be used as Soffos AI source
        '''
        return self._document_ids

    @document_ids.setter
    def document_id(self, value):
        self._document_id = value
        self.concern = value

    @property
    def tagged_elements(self):
        return self._tagged_elements

    @tagged_elements.setter
    def tagged_elements(self, value):
        self._tagged_elements = value

    @property
    def user_answer(self) -> str:
        '''
        The answer of an end user to be evaluated on answer scoring
        '''
        return self._user_answer
    
    @user_answer.setter
    def user_answer(self, value):
        self._user_answer = value
        self.concern = value

    @property
    def sentence_overlap(self) -> bool:
        '''
        Whether to overlap adjacent chunks by 1 sentence. 
        For example, with sentence_split 3 and sentence_overlap=true :
        [[s1, s2, s3], [s3, s4, s5], [s5, s6, s7]]
        '''
        return self._sentence_overlap

    @sentence_overlap.setter
    def sentence_overlap(self, value) -> bool:
        self._sentence_overlap = value

    @property
    def sentence_split(self):
        '''
        how many sentences per evaluation of ambiguity
        '''
        return self._sentence_split

    @sentence_split.setter
    def sentence_split (self,value):
        self._sentence_split = value

    @property
    def normalize(self)->bool:
        '''
        returns the normalize flag value of file converter
        '''
        return self._normalize

    @normalize.setter
    def normalize(self,value)->int:
        '''
        sets the normalize flag value of file converter
        '''
        self._normalize = value

    @property
    def charged_character_count(self) -> int:
        '''
        The character count that is billed. It depends on which is higher: the request or the response.
        '''
        return self._charged_character_count
    
    @property
    def user(self) -> str:
        '''
        The end_user identification
        '''
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value

    @property
    def service(self) -> str:
        '''
        What do you want Soffos AI to think off?
        ----------------------------------------
        '''
        return self._service

    @service.setter
    def service(self, value):
        if value not in SERVICES_LIST:
            raise KeyError(f"Invalid Service please choose from {SERVICES_LIST} or import Services for faster coding")
        
        self._service = value
        
    @property
    def output_key(self) -> str:
        return self._output_key

    @output_key.setter
    def output_key(self, value):
        self._output_key = value

    @property
    def src(self):
        '''
        The source of truth for Soffos API Comprehension
        '''
        return self._src

    @src.setter
    def src(self, value):
        self._src = value
        if isinstance(value, dict):
            if "document_id" in value.keys():
                self._document_id = value['document_id']
        
        elif isinstance(value, str):
            if is_valid_uuid(value):
                self._document_id = value
                
    @property
    def concern(self) -> str:
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._concern

    @concern.setter
    def concern(self, value):
        self._concern = value

    @property
    def question(self) -> str:
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
        self._concern = value


    def get_response(self, output_key=None) -> str:
        '''
        Based on the source/concern, Soffos AI will now give you the data you need
        '''
        if not self._service:
            raise AttributeError("Please provide the service type you need from Soffos AI.")
        
        if not self._user:
            raise AttributeError("user is required")

        service:SoffosAIService = SERVICE_CLASS_MAP[self._service](
            apikey=self._apikey,
            user=self._user,
            src=self._src,
            concern=self._concern,
            document_ids=self._document_ids,
            normalize=self._normalize,
            sentence_split = self._sentence_split,
            sentence_overlap = self._sentence_overlap,
            tagged_elements = self._tagged_elements
        )

        json_response:dict = service.process_request()

        if not output_key:
            output_key = self._output_key

        if not output_key:
            primary_output_key = service.get_default_output_key()
            secondary_output_key = service.get_default_secondary_output_key()
            output_key = primary_output_key if primary_output_key in json_response.keys() else secondary_output_key

        try:
            response = json_response[output_key]
        except KeyError:
            print("Error on Response. Output key is not found")
            response = json_response

        return SoffosAiResponse(
            raw = json_response,
            response = response,
            context = json_response.get('context'),
            cost = json_response.get('cost'),
            charged_character_count = json_response.get('charged_character_count'),
            tagged_elements = json_response.get("tagged_elements"),
            document_ids=json_response.get("document_ids")
        )
