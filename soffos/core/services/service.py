'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The main module of Soffos
-----------------------------------------------------
'''
import abc, http3
from soffos.common.constants import SOFFOS_SERVICE_URL

class SoffosAIService:
    '''
    Base service class for all Soffos Services
    '''
    def __init__(self, apikey, src=None, concern=None) -> None:
        self.headers = {
            "x-api-key": apikey,
            "content-type": "application/json"
        }
        self._apikey = apikey
        self._src = src
        self._concern = concern
        self._service = None

    @abc.abstractmethod
    def allow_input(self, value):
        '''
        checks if the input type is allowed for the service
        '''

    @abc.abstractmethod
    def provide_output_type(self):
        '''
        Sends back the output datatype of the service
        '''
    
    @abc.abstractmethod
    def provide_source_type(self):
        '''
        Sends back the accepted source datatype of the service
        '''

    @abc.abstractmethod
    def provide_concern_type(self):
        '''
        Sends back the accepted concern datatype of the service
        '''

    @abc.abstractmethod
    def get_default_output_key(self):
        '''
        Sends back the output type of the service
        '''

    @abc.abstractmethod
    def get_json(self):
        '''
        Prepare json input of the service
        '''

    def _get_response(self):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        # if not self.output_key:
        #     self.output_key = self.get_default_output_key()

        response = http3.post(
            url=SOFFOS_SERVICE_URL + self._service + "/",
            headers=self.headers,
            json=self.get_json(),
            timeout=30
        )
        return response.json()

    def process_request(self):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        allow_input, message = self.allow_input(self._src, self._concern)
        
        if not allow_input:
            raise ValueError(message)
        
        if not self._service:
            raise ValueError("Please provide a service you need from Soffos AI.")

        return self._get_response()
