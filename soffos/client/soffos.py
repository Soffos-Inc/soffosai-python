'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''

from soffos.common.constants import SERVICES_LIST, Services
from soffos.core.services import QuestionAnsweringService

SERVICE_CLASS_MAP = {
    Services.QUESTION_ANSWERING: QuestionAnsweringService
}

class Client:
    '''
    Not finished yet -- Just warming up
    ------------------------------------
    handles Soffos API http requests
    '''

    def __init__(self, apikey) -> dict:

        self._apikey = apikey
        # self.service = None
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
        self.context = None

    @property
    def service(self):
        '''
        What do you want Soffos AI to think off?
        ----------------------------------------
        '''
        return self._service


    @service.setter
    def service(self, value):
        if value not in SERVICES_LIST:
            raise KeyError(f"Invalid Service please choose from {SERVICES_LIST} or import Services for faster coding")
        
        self.context = None
        self._service = value
        

    @property
    def output_key(self):
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
        self.context = None
        self._src = value


    @property
    def concern(self):
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._concern


    @concern.setter
    def concern(self, value):
        self.context = None
        self._concern = value

    
    @property
    def question(self):
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._question


    @question.setter
    def question(self, value):
        self.context = None
        self._question = value
        self._concern = value


    def get_response(self, output_key=None):
        '''
        Based on the source/context, Soffos AI will now give you the data you need
        '''
        if not self._service:
            raise ValueError("Please provide the service type you need from Soffos AI.")

        service = SERVICE_CLASS_MAP[self._service](
            apikey=self._apikey,
            # output_key=output_key,
            src=self._src,
            concern=self._concern
        )
        if not output_key:
            output_key = service.get_default_output_key()

        json_response = service.process_request()
        response = json_response[output_key]
        self.context = json_response.get('context')
        return response
