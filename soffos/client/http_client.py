'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''
import os
import http3
import requests
import mimetypes
import soffos
from soffos.common.constants import SOFFOS_SERVICE_URL


class HttpClient:
    '''
    handles http requests
    '''

    def __init__(
        self, headers, service, data=None, json=None, file=None):
        self._headers = headers
        self._service = service
        self._data = data
        self._json = json
        self._file = file
        self._apikey = soffos.api_key
        self.headers = {
                    "x-api-key": self._apikey,
                    "Content-Type": "application/json"
                }


    @classmethod
    def get_response(self) -> dict:
        '''
        Based on the source/concern, Soffos AI will now give you the data you need
        '''
        response = None
        if self._json:
            response = http3.post(
                url=SOFFOS_SERVICE_URL + self._service + "/",
                headers=self.headers,
                json=self._json,
                timeout=60
            )
            
        elif self._data:
            data = self._data
            filename = str(os.path.basename(self._file))
            mime_type, _ = mimetypes.guess_type(self._file)
            with open(self._file, 'rb') as file:
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
            return {"error": response}
            # raise ValueError(response)
