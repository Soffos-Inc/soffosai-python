'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Soffos Services Objects
-----------------------------------------------------
'''

from .service import SoffosAIService

from .question_answering import QuestionAnsweringService
from .file_converter import FileConverterService
from .ambiguity_detection import AmbiguityDetectionService
from .answer_scoring import AnswerScoringService
from .contradiction_detection import ContradictionDetectionService
from .documents import DocumentsIngestService, DocumentsSearchService, DocumentsDeleteService
from .service import is_valid_uuid
