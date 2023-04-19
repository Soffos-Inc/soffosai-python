'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-19
Purpose: Hold the output response of Soffos API in an object
-----------------------------------------------------
'''
import json

class SoffosAiResponse:
    '''
    Holds the Soffos AI response
    '''
    def __init__(self, context=None, raw=None, cost=None, charged_character_count=0, response=None, tagged_elements=None, document_ids=None,**kwargs) -> None:
        self._context = context
        self._raw = raw
        self._cost = cost
        self._charged_character_count = charged_character_count
        self._response = response
        self._tagged_elements = tagged_elements
        self._document_ids = document_ids

    @property
    def context(self):
        '''
        The context where the reply is based on
        '''
        return self._context

    @property
    def raw_response(self) -> dict:
        '''
        The raw json response from the ai but converted into a dictionary
        '''
        return self._raw

    @property
    def cost(self) -> dict:
        '''
        a dictionary describing the cost of the api call
        '''
        return self._cost

    @property
    def charged_character_count(self):
        '''
        The number of characters charged. It is based on input or output whichever is higher
        '''
        return self._charged_character_count

    @property
    def response(self) -> str or dict:
        '''
        The common response
        '''
        return self._response

    @property
    def tagged_elements(self):
        '''
        The tagged elements that can be used to optimize document ingestion.
        This is an output of the file converter and is useful for the document ingestion service
        '''
        return self._tagged_elements

    @property
    def document_ids(self):
        return self._document_ids

    def __str__(self) -> str:
        return self._response if isinstance(self._response, str) else json.dumps(self._response)
