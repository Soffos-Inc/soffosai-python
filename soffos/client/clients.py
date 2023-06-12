'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-19
Purpose: Specific Soffos Client per service
-----------------------------------------------------
'''
from .http_client import HttpClient as Client
from soffos.core.services import *
from soffos.common.constants import ServiceString


class AmbiguityDetectionClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.AMBIGUITY_DETECTION


class AnswerScoringClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.ANSWER_SCORING


class ContradictionDetectionClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.CONTRADICTION_DETECTION


class DocumentIngestClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.DOCUMENTS_INGEST


class DocumentSearchClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.DOCUMENTS_SEARCH


class DocumentDeleteClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.DOCUMENTS_DELETE


class FileConverterClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.FILE_CONVERTER


class QuestionAnsweringClient(Client):
    def __init__(self, apikey, user=None) -> dict:
        super().__init__(apikey, user)
        self._service = ServiceString.QUESTION_ANSWERING

