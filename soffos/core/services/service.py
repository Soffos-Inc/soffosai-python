'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The base Service class
-----------------------------------------------------
'''
import soffos
import abc, http3, requests, os, mimetypes, uuid, json
from soffos.common.constants import SOFFOS_SERVICE_URL, ServiceString, FORM_DATA_REQUIRED
from soffos.client.http_client import HttpClient
from soffos.common.service_io_map import SERVICE_IO_MAP
from soffos.common.serviceio_fields import ServiceIO


visit_docs_message = "Kindly visit https://platform.soffos.ai/playground/docs#/ for guidance."
input_structure_message = "To learn what the input dictionary should look like, access it by <your_service_instance>.input_structure"


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
    def __init__(self, service, user=None, src=None, **kwargs) -> None:            
        if kwargs.get("apikey"):
            apikey = kwargs['apikey']
        else:
            apikey = soffos.api_key
            
        self.headers = {
            "x-api-key": apikey,
        }
        self._apikey = apikey
        self._src = src
        self._user = user
        self._service = service
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(service)

    @property
    def input_structure(self):
        '''
        These are the valid fields of the src dictionary for this service. Take note that some of the fields should not exist at the same time.
        To view fields that cannot co-exist, access the 'choose_one' property.
        '''
        return self._serviceio.input_structure
    
    @property
    def choose_one(self):
        '''
        These keys cannot co-exist in this service's src.
        '''
        return self._serviceio.require_one_of_choice

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value

    def allow_input(self):
        '''
        checks if the input type is allowed for the service
        '''
        if not isinstance(self._src, dict):
            raise TypeError("src should be a dictionary")

        user_from_src = self._src.get('user')
        if user_from_src:
            self._user = user_from_src
        
        if not self._user:
            return False, "user argument is not provided as constructor argument nor in the src keys"

        if len(self._serviceio.required_input_fields) > 0:
            missing_requirements = []
            for required in self._serviceio.required_input_fields:
                if required not in self._src:
                    missing_requirements.append(required)
            if len(missing_requirements) > 0:
                return False, f"Please provide {missing_requirements} on your src. {visit_docs_message}. {input_structure_message}"
        
        if len(self._serviceio.require_one_of_choice) > 0:
            group_error = []
            for group in self._serviceio.require_one_of_choice:
                found_choices = []
                for choice in group:
                    if choice in self._src:
                        found_choices.append(choice)
                if len(found_choices) == 0:
                    group_error.append(f"Please provide one of these values on your source: {group}")
                elif len(found_choices) > 1:
                    group_error.append(f"Please only include one of these values: {group}")

            if len(group_error) > 0:
                return False, group_error
        
        if "document_ids" in self._src:
            for _id in self._src["document_ids"]:
                valid_uuid = is_valid_uuid(_id)
                if not valid_uuid:
                    return False, f"{_id} is invalid document_id"
        
        return True, None


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
    def get_default_output_key(self):
        '''
        Sends back the output type of the service
        '''
    

    def get_data(self):
        '''
        Prepare the json or form data input of the service
        '''
        
        request_data = {
            "user": self._user
        }
        for key, value in self._src.items():
            if key != 'file':
                request_data[key] = value

        return request_data


    def get_response(self, src=None):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        if src:
            self._src = src
        
        if 'user' in src.keys():
            self._user = src['user']

        allow_input, message = self.allow_input()
        if not allow_input:
            raise ValueError(message)
        
        if not self._service:
            raise ValueError("Please provide the service you need from Soffos AI.")

        response = None
        data = self.get_data()

        if self._service not in FORM_DATA_REQUIRED:
            self.headers["content-type"] = "application/json"
            response = http3.post(
                url = SOFFOS_SERVICE_URL + self._service + "/",
                headers = self.headers,
                json = data,
                timeout = 60
            )
            
        else:
            file_path = self._src.get('file')
            filename = str(os.path.basename(file_path))
            mime_type, _ = mimetypes.guess_type(file_path)
            with open(file_path, 'rb') as file:
                files = {
                    "file": (filename, file, mime_type)
                }

                response = requests.post(
                    url = SOFFOS_SERVICE_URL + self._service + "/",
                    headers = self.headers,
                    data = data,
                    files = files,
                )
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as err:
            raise ValueError(response) from err
        except AttributeError as err2:
            raise AttributeError(str(err2)) from err2
