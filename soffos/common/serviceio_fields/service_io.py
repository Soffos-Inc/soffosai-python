'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-19
Purpose: Maps the input and output fields of services
-----------------------------------------------------
'''
from ..constants import Services

class ServiceIO:
    '''
    Defines the IO of services. The structure is specifically important to determine if
    the input provided by the programmer or other service is acceptable
    '''
    service = None
    required_input_fields = []
    require_one_of_choice = []
    input_structure = {}
    optional_input_fields = []
    output_structure = {}
    def __init__(self) -> None:
        self._output_fields = list(self.output_structure.keys())
    
    @property
    def output_fields(self):
        return self._output_fields
