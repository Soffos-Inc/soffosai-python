'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''

from soffos.common.constants import SERVICES_LIST, Services
from soffos.core.services import QuestionAnsweringService, FileConverterService

SERVICE_CLASS_MAP = {
    Services.QUESTION_ANSWERING: QuestionAnsweringService,
    Services.FILE_CONVERTER: FileConverterService
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
    def src(self) -> str:
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
            concern=self._concern
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
