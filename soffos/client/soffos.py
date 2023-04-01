'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''

import requests
import http3
from soffos.common.constants import SERVICES_LIST, SOFFOS_SERVICE_URL

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
        self._input = None
        self._question = None
        self._answer = None
        self._tags = None
        self._knowledge = None

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

        self._service = value


    @property
    def input(self):
        '''
        The source of truth for Soffos API Comprehension
        '''
        return self._input


    @input.setter
    def input(self, value):
        self._input = value


    @property
    def question(self):
        '''
        What do want to know about the knowledge you ingested
        '''
        return self._question


    @question.setter
    def question(self, value):
        self._question = value
        self._input = value


    @property
    def knowledge(self):
        '''
        The data that Soffos AI will accept as truth and will find answer from
        '''
        return self._knowledge


    @knowledge.setter
    def knowledge(self, value):
        self._knowledge = value


    def get_response(self):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        response = http3.post(
            url=SOFFOS_SERVICE_URL + self.service + "/",
            headers=self.headers,
            json={
                "user": self._apikey,
                "message": self.question,
                "document_text": self.knowledge
            },
            timeout=30
        )
        return response.json()