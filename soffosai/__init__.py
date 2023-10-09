'''
Soffos Inc. Python SDK package
'''

from .client import SoffosAiResponse
from .common.constants import ServiceString
from .core.pipelines import SoffosPipeline, FileIngestPipeline, FileSummaryPipeline, DocumentSummaryPipeline
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
)
from .common.constants import ServiceString
from .core import services as SoffosAIServices
from .core import pipelines as SoffosAIPipelines
import os

api_key = os.environ.get("SOFFOSAI_API_KEY")

__all__ = [
    "api_key",
    "ServiceString",
    "SoffosAiResponse",
    "SoffosAIServices",
    "SoffosAIPipelines",
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

    "SoffosPipeline", 
    "FileIngestPipeline", 
    "FileSummaryPipeline", 
    "DocumentSummaryPipeline"
]

__title__ = "soffosai"
__description__ = "Python SDK for Soffos.ai API"
__version__ = "0.0.3"
