'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Soffos Services Objects
-----------------------------------------------------
'''

from .service import SoffosAIService, inspect_arguments
from .ambiguity_detection import AmbiguityDetectionService
from .answer_scoring import AnswerScoringService
from .contradiction_detection import ContradictionDetectionService
from .documents import DocumentsIngestService, DocumentsSearchService, DocumentsDeleteService, DocumentsService
from .email_analysis import EmailAnalysisService
from .emotion_detection import EmotionDetectionService
from .file_converter import FileConverterService
from .language_detection import LanguageDetectionService
from .lets_discuss import LetsDiscussService, LetsDiscussCreateService, LetsDiscussRetrieveService, LetsDiscussDeleteService
from .logical_error_detection import LogicalErrorDetectionService
from .microlesson import MicrolessonService
from .NER import NamedEntityRecognitionService
from .paraphrase import ParaphraseService
from .profanity import ProfanityService
from .qna_generation import QuestionAndAnswerGenerationService
from .question_answering import QuestionAnsweringService
from .review_tagger import ReviewTaggerService
from .sentiment_analysis import SentimentAnalysisService
from .simplify import SimplifyService
from .summarization import SummarizationService
from .table_generator import TableGeneratorService
from .tag_generation import TagGenerationService
from .transcript_correction import TranscriptCorrectionService
from .input_config import InputConfig
