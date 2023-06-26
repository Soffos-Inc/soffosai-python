'''
Soffos Inc. Python SDK package
'''

from .client import SoffosAiResponse
from .common.constants import ServiceString
from .core.services import (
    AmbiguityDetectionService, 
    AnswerScoringService, 
    ContradictionDetectionService,
    DocumentsIngestService, DocumentsSearchService, DocumentsDeleteService, DocumentsService,
    EmailAnalysisService,
    FileConverterService,
    LanguageDetectionService,
    LetsDiscussService,
    LogicalErrorDetectionService,
    MicrolessonService,
    NamedEntityRecognitionService,
)
import os
import sys

api_key = os.environ.get("SOFFOSAI_API_KEY")

__all__ = [
    "api_key",
    "ServiceString",
    "SoffosAiResponse",
    "AmbiguityDetectionService",
    "AnswerScoringService",
    "ContradictionDetectionService",
    "DocumentsIngestService", "DocumentsSearchService", "DocumentsDeleteService", "DocumentsService",
    "EmailAnalysisService",
    "FileConverterService",
    "LanguageDetectionService",
    "LetsDiscussService",
    "LogicalErrorDetectionService",
    "MicrolessonService",
    "NamedEntityRecognitionService",
]
