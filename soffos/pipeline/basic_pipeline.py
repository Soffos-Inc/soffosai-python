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


class SoffosPipeline:
    def __init__(self, stages=[], sources={}) -> None:
        self._stages = stages
        self._sources:dict = sources
        error_messages = []
        for stage in self._stages:
            if stage not in SERVICES_LIST:
                error_messages.append(f"{stage} is not a valid Soffos Service")
        if len(error_messages) != 0:
            raise ValueError(error_messages)
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
        available_sources = list(self._sources.keys())

        if previous_stage:
            previous_service_io: ServiceIO = SERVICE_IO_MAP[previous_stage]
            available_sources.extend(previous_service_io.output_fields)

        for field in _serviceio.required_input_fields:
            if field not in available_sources:
                error_messages.append(f"{field} is required by {current_stage}. Please add this to the sources")
        
        for field_list in _serviceio.require_one_of_choice:
            fields_given = []
            for field in field_list:
                if field in available_sources:
                    fields_given.append(field)
            
            if len(fields_given) == 0:
                error_messages.append(f"Please provide only one of these fields: {field_list}")
            
            if len(fields_given) > 1:
                error_messages.append(f"Only one of these fields should be provided: {field_list} but {len(fields_given)} is given")

        if len(error_messages) > 0:
            return False, error_messages
        else:
            return True, None
