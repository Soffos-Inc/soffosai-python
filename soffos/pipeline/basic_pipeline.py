'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-21
Purpose: Define the basic pipeline object
-----------------------------------------------------
'''
from soffos.common import serviceio_fields as serviceio
from soffos.common.constants import Services, SERVICES_LIST
from soffos.common.service_io_map import SERVICE_IO_MAP
from soffos.common.serviceio_fields import ServiceIO
from soffos.client import Client, SoffosAiResponse


class SoffosPipeline:
    def __init__(self, apikey, user, stages:list, sources=dict) -> None:
        self._apikey = apikey
        self._stages = stages
        self._user = user
        self._sources:dict = sources
        self._available_sources = list(self._sources.keys())
        self._concern = None

        error_messages = []
        if not isinstance(stages, list):
            error_messages.append("stages field should be a list of Soffos Services")
        if not isinstance(sources, dict):
            error_messages.append("sources should be a dictionary of required inputs")
        for stage in self._stages:
            if stage not in SERVICES_LIST:
                error_messages.append(f"{stage} is not a valid Soffos Service")
        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        if "text" in self._sources.keys():
            self._sources["document_text"] = self._sources["text"]
            
        self.validate_pipeline()


    def validate_pipeline(self):
        error_messages = []
        previous_stage = None
        current_stage = None
        for i, stage in enumerate(self._stages):
            current_stage = stage
            if i > 0:
                previous_stage = self._stages[i-1]
            stage_valid, errors = self.check_stage_input(previous_stage, current_stage)
            if not stage_valid:
                error_messages.extend(errors)
        
        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        return True


    def check_stage_input(self, previous_stage, current_stage):
        _serviceio:ServiceIO = SERVICE_IO_MAP[current_stage]
        error_messages = []
        # print(f"validating input of stage: {current_stage}")
        # print(f"current available sources: {self._available_sources}")
        if previous_stage:
            previous_service_io: ServiceIO = SERVICE_IO_MAP[previous_stage]()
            self._available_sources.extend(previous_service_io.output_fields)
            if "text" in self._available_sources:
                self._available_sources.append("document_text")

        for field in _serviceio.required_input_fields:
            if field == "text" and "context" in self._available_sources:
                self._available_sources.append("context")
                continue
            if field == "context" and "text" in self._available_sources:
                self._available_sources.append("text")
                continue
            if field not in self._available_sources:
                error_messages.append(f"{field} is required by {current_stage}. Please add this to the sources")
        
        for field_list in _serviceio.require_one_of_choice:
            fields_given = []
            for field in field_list:
                if field in self._available_sources:
                    fields_given.append(field)
            
            if len(fields_given) == 0:
                error_messages.append(f"{current_stage}: Please provide only one of these fields: {field_list}")
            
            # if len(fields_given) > 1:
            #     error_messages.append(f"{current_stage}: Only one of these fields should be provided: {field_list} but {len(fields_given)} is given")

        if len(error_messages) > 0:
            return False, error_messages
        else:
            return True, None

        
    def run(self) -> dict:
        collected_responses = {}
        for stage in self._stages:
            response = {}
            _serviceio:ServiceIO = SERVICE_IO_MAP[stage]
            prepared_input = {}
            for required_input in _serviceio.required_input_fields:
                if required_input not in self._sources:
                    raise ValueError(f"required input: {required_input} not found in sources")
                prepared_input[required_input] = self._sources[required_input]
                if required_input == "message":
                    self._concern = self._sources[required_input]
            
            for group_choices in _serviceio.require_one_of_choice:
                for field in group_choices:
                    if field in self._sources.keys():
                        prepared_input[field]= self._sources[field]
                        break
                    if field == "document_text":
                        prepared_input["document_text"] = self._sources.get("text")
            
            for optional_field in _serviceio.optional_input_fields:
                if optional_field in self._sources:
                    prepared_input[optional_field] = self._sources[optional_field]
            
            prepared_input_keys = list(prepared_input.keys())
            print(f"prepared input keys for {stage}: {prepared_input_keys}")

            client = Client(
                service=stage,
                apikey=self._apikey,
                user=self._user,
                src=prepared_input,
                concern=self._concern
            )
            print(f"calling {stage}")
            response:SoffosAiResponse = client.get_response()
            new_keys = list(response.raw_response.keys())
            print(f"response keys: {new_keys}")
            collected_responses[stage] = response.raw_response
            self._sources.update(response.raw_response)
            updated_src_keys = list(self._sources.keys())
            print(f"updated sources keys: {updated_src_keys}")
        
        return collected_responses
