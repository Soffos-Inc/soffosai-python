'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Easily use Website Converter Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class WebsiteConverterService(SoffosAIService):
    '''
    The Website Converter module offers basic functionality for extracting
    meaningful text from websites. This can be a useful tool for processing website
    content with other modules. Note: Character volume is not charged for this
    module.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.WEBSITE_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, url:str) -> dict:
        '''
        Call the Website Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param url: The url to extract text from.
        :return: text: Raw text extracted from the website.
        links: A dictionary containing a list of `internal` and a list of `external`
            links found on the website. `internal`: Links found on the page that are
            under the same domain as the provided url. `external`: Links found on the
            page that belong to different domains.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/website_converter.py>`_
        '''
        return super().__call__(user=user, url=url)

    def set_input_configs(self, name:str, url:Union[str, InputConfig]):
        super().set_input_configs(name=name, url=url)

    @classmethod
    def call(self, user:str, url:str) -> dict:
        '''
        Call the Website Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param url: The url to extract text from.
        :return: text: Raw text extracted from the website.
        links: A dictionary containing a list of `internal` and a list of `external`
            links found on the website. `internal`: Links found on the page that are
            under the same domain as the provided url. `external`: Links found on the
            page that belong to different domains.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/website_converter.py>`_
        '''
        return super().call(user=user, url=url)

