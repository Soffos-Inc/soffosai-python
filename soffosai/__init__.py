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
    EmotionDetectionService,
    FileConverterService,
    LanguageDetectionService,
    LetsDiscussService,
    LogicalErrorDetectionService,
    MicrolessonService,
    NamedEntityRecognitionService,
    ParaphraseService,
    ProfanityService,
    QuestionAndAnswerGenerationService,
    QuestionAnsweringService,
    ReviewTaggerService,
    SentimentAnalysisService,
    SimplifyService,
    SummarizationService,
    TableGeneratorService,
    TagGenerationService,
    TranscriptCorrectionService,

    inspect_arguments
)
from .common.constants import ServiceString

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
    "EmotionDetectionService",
    "FileConverterService",
    "LanguageDetectionService",
    "LetsDiscussService",
    "LogicalErrorDetectionService",
    "MicrolessonService",
    "NamedEntityRecognitionService",
    "ParaphraseService",
    "ProfanityService",
    "QuestionAndAnswerGenerationService",
    "QuestionAnsweringService",
    "ReviewTaggerService",
    "SentimentAnalysisService",
    "SimplifyService",
    "SummarizationService",
    "TableGeneratorService",
    "TagGenerationService",
    "TranscriptCorrectionService",

    "ServiceString"
]
