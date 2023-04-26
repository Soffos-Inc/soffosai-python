'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The base Service class
-----------------------------------------------------
'''
import abc, http3, requests, os, mimetypes, uuid, json
from soffos.common.constants import SOFFOS_SERVICE_URL


def is_valid_uuid(uuid_string):
    try:
        uuid_obj = uuid.UUID(uuid_string)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_string


class SoffosAIService:
    '''
    Base service class for all Soffos Services
    '''
    def __init__(self, apikey, user, src=None, concern=None, document_id=None, **kwargs) -> None:
        self.headers = {
            "x-api-key": apikey,
            "content-type": "application/json"
        }
        self._apikey = apikey
        self._src = src
        self._concern = concern
        self._service = None
        self._user = user
        self._document_id = document_id
        if isinstance(src, dict):
            for key in src.keys():
                if isinstance(src[key], str):
                    if is_valid_uuid(src[key]):
                        self._document_id = src[key]

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
    def get_default_secondary_output_key(self):
        '''
        Sends back a secondary output type of the service if existing
        '''

    def get_json(self):
        '''
        Prepare json input of the service
        '''
        return None
    
    def get_data(self):
        '''
        Prepare the form data input of the service
        '''
        return None

    def _get_response(self):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        response = None
        print(json.dumps(self.get_json(), indent=4))
        if self.get_json():
            response = requests.post(
                url=SOFFOS_SERVICE_URL + self._service + "/",
                headers=self.headers,
                json=self.get_json(),
                # timeout=30
            )
            
        elif self.get_data():
            data = self.get_data()
            filename = str(os.path.basename(self._src))
            mime_type, _ = mimetypes.guess_type(self._src)
            with open(self._src, 'rb') as file:
                files = {
                    "file": (filename, file, mime_type)
                }
                self.headers = {
                    'x-api-key': self._apikey
                }
                response = requests.post(
                    url=SOFFOS_SERVICE_URL + self._service + "/",
                    headers=self.headers,
                    data=data,
                    files=files,
                )
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as err:
            raise ValueError(response)


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
