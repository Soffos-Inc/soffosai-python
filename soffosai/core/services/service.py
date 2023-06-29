'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The base Service class
-----------------------------------------------------
'''
import inspect
import soffosai
import json
import abc, http3, requests, os, mimetypes, uuid
from soffosai.common.constants import SOFFOS_SERVICE_URL, FORM_DATA_REQUIRED
from soffosai.common.service_io_map import SERVICE_IO_MAP
from soffosai.common.serviceio_fields import ServiceIO


visit_docs_message = "Kindly visit https://platform.soffos.ai/playground/docs#/ for guidance."
input_structure_message = "To learn what the input dictionary should look like, access it by <your_service_instance>.input_structure"


def inspect_arguments(func, *args, **kwargs):
    '''
    Given a function, args and kwargs: 
    create a dictionary with keys as the arg names and values as the arg values
    '''
    # Get the list of argument names
    sig = inspect.signature(func)
    arg_names = list(sig.parameters.keys())

    # Combine positional arguments and keyword arguments
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    combined_args = bound_args.arguments

    # Filter out positional arguments not present in arg_names
    arguments = {name: combined_args[name] for name in arg_names if name in combined_args}
    unziped_kwargs = {}
    for key,value in arguments.items():
        if key != "kwargs":
            if value != None:
                unziped_kwargs[key] = value
        else:
            for key2, value2 in arguments['kwargs'].items():
                if value2 != None:
                    unziped_kwargs[key2] = value2

    return unziped_kwargs


def format_uuid(uuid):
    formatted_uuid = '-'.join([
        uuid[:8],
        uuid[8:12],
        uuid[12:16],
        uuid[16:20],
        uuid[20:]
    ])
    return formatted_uuid


def is_valid_uuid(uuid_string):
    if isinstance(uuid_string, type): # coming from pipeline validation, always True because it will come from Soffos Services
        return True

    if "-" not in uuid_string:
        formatted_uuid = format_uuid(uuid_string)
    else:
        formatted_uuid = uuid_string
    try:
        uuid_obj = uuid.UUID(formatted_uuid)
    except ValueError:
        return False
    return str(uuid_obj) == formatted_uuid


class SoffosAIService:
    '''
    Base service class for all Soffos Services
    '''
    def __init__(self, service:str, **kwargs) -> None:            
        if kwargs.get("apikey"):
            apikey = kwargs['apikey']
        else:
            apikey = soffosai.api_key
            
        self.headers = {
            "x-api-key": apikey,
        }
        self._apikey = apikey
        self._service = service
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(service)
        self._payload = {}
        self._payload_keys = self._payload.keys()
        self._args_dict = {}


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


    def validate_payload(self):
        '''
        checks if the input type is allowed for the service
        '''
        if not isinstance(self._payload, dict):
            raise TypeError("payload should be a dictionary")

        # check for missing arguments
        user_from_src = self._payload.get('user')
        if not user_from_src:
            return False, f"{self._service}: user key is required in the payload"

        if len(self._serviceio.required_input_fields) > 0:
            missing_requirements = []
            for required in self._serviceio.required_input_fields:
                if required not in self._payload:
                    missing_requirements.append(required)
            if len(missing_requirements) > 0:
                return False, f"{self._service}: Please provide {missing_requirements} on your payload. {visit_docs_message}. {input_structure_message}"
        
        if len(self._serviceio.require_one_of_choice) > 0:
            group_error = []
            for group in self._serviceio.require_one_of_choice:
                found_choices = []
                for choice in group:
                    if choice in self._payload:
                        found_choices.append(choice)
                if len(found_choices) == 0:
                    group_error.append(f"{self._service}: Please provide one of these values on your payload: {group}")
                elif len(found_choices) > 1:
                    group_error.append(f"{self._service}: Please only include one of these values: {group}")
            
            if len(group_error) > 0:
                return False, group_error

        # check if payload has proper type:
        input_structure = self._serviceio.input_structure
        value_errors = []
        for key, value in self._payload.items():
            if key in input_structure.keys():

                if not isinstance(input_structure[key], type):
                    input_type = type(input_structure[key])
                else:
                    input_type = input_structure[key]

                if not isinstance(value, input_type) and value != input_type: # the second condition is for pipeline
                    wrong_type = type(value)
                    value_errors.append(f"{key} requires {input_structure[key]} but {wrong_type} is provided.")
            
        if len(value_errors) > 0:
            return False, value_errors

        if "document_ids" in self._payload:
            if isinstance(self._payload['document_ids'], list):
                for _id in self._payload["document_ids"]:
                    valid_uuid = is_valid_uuid(_id)
                    if not valid_uuid:
                        return False, f"{_id} is invalid document_id"
        
        return True, None

     
    def update_payload(self, key, value):
        if key in self._payload_keys:
            print(f"Warning:overwriting payload[{key}]")
        self._payload[key] = value


    def get_data(self):
        '''
        Prepare the json or form data input of the service
        '''
        
        request_data = {}
        for key, value in self._payload.items():
            if key != 'file':
                request_data[key] = value

        return request_data


    def get_response(self, payload={}, **kwargs):
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        self._payload = payload
        allow_input, message = self.validate_payload()
        if "question" in self._payload.keys(): # the api receives the question as message.
            self._payload['message'] = self._payload['question']

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
            file_path = self._payload.get('file')
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
            return response
        except json.decoder.JSONDecodeError as err:
            return response
        except AttributeError as err:
            raise AttributeError(str(err)) from err


    def __call__(self, **kwargs):

        return self.get_response(payload=self._args_dict,**kwargs)


    def __str__(self) -> str:
        return self._service


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
