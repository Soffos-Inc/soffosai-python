'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''

from soffos.common.constants import SERVICES_LIST, Services
from soffos.core.services import *

SERVICE_CLASS_MAP = {
    Services.QUESTION_ANSWERING: QuestionAnsweringService,
    Services.FILE_CONVERTER: FileConverterService,
    Services.AMBIGUITY_DETECTION: AmbiguityDetectionService,
    Services.ANSWER_SCORING: AnswerScoringService
}

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
        
        # read-only attributes
        self._context = None
        self._raw = None
        self._cost = None
        self._charged_character_count = 0
        self._response = None
    
    @property
    def response(self) -> str:
        '''
        The main response[key] is saved here
        '''
        return self._response

    @property
    def raw_response(self) -> dict:
        '''
        View the raw response of the last soffos api called
        '''
        return self._raw
    
    @property
    def user_answer(self) -> str:
        '''
        The answer of an end user to be evaluated on answer scoring
        '''
        return self._user_answer
    
    @user_answer.setter
    def user_answer(self, value):
        self._user_answer = value
        self._concern = value
        self._context = None

    @property
    def sentence_overlap(self) -> bool:
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
    def cost(self) -> dict:
        '''
        The costing detail of the last get_response() call
        '''
        return self._cost

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
    def context(self) -> str:
        '''
        The context where the response is based off.  When the document is ingested, only part of it
        has the context and only that will be included on billing not the whole document.
        '''
        return self._context

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
        
        self._context = None
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
        self._context = None
        self._src = value


    @property
    def concern(self) -> str:
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._concern


    @concern.setter
    def concern(self, value):
        self._context = None
        self._concern = value

    
    @property
    def question(self) -> str:
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._question


    @question.setter
    def question(self, value):
        self._context = None
        self._question = value
        self._concern = value


    def get_response(self, output_key=None) -> str:
        '''
        Based on the source/context, Soffos AI will now give you the data you need
        '''
        if not self._service:
            raise AttributeError("Please provide the service type you need from Soffos AI.")
        
        if not self._user:
            raise AttributeError("user is required")

        service = SERVICE_CLASS_MAP[self._service](
            apikey=self._apikey,
            user=self._user,
            src=self._src,
            concern=self._concern,
            normalize=self._normalize,
            sentence_split = self._sentence_split
        )

        if not output_key:
            primary_output_key = service.get_default_output_key()
            secondary_output_key = service.get_default_secondary_output_key()

        json_response = service.process_request()

        self._raw = json_response
        output_key = primary_output_key if primary_output_key in json_response.keys() else secondary_output_key
        try:
            self._response = json_response[output_key]
        except KeyError:
            self._response = json_response

        self._context = json_response.get('context')
        self._cost = json_response.get('cost')
        self._charged_character_count = json_response.get('charged_character_count')

        return self._response
