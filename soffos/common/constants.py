'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-19
Purpose: Organize the constants
-----------------------------------------------------
'''

SOFFOS_SERVICE_URL = "https://dev-api.soffos.ai/service/"

SERVICES_LIST = [
    'ambiguity-detection',
    'answer-scoring', 
    'contradiction-detection', 
    'discuss', 
    'documents/ingest', 
    'email-analysis', 
    'emotion-detection', 
    'file-converter', 
    'flashcard-generation', 
    'intent-classification/confirmation', 
    'intent-classification', 
    'language-detection', 
    'microlesson', 
    'ner', 
    'paraphrase', 
    'profanity',
    'qna-generation',
    'question-answering',
    'review-tagger',
    'search-recommendations',
    'sentiment-analysis',
    'simplify',
    'string-similarity',
    'summarization',
    'tag',
    'transcript-correction',
    'batch-service/'
]

class Services:
    '''
    Contains the list of Soffos services as attributes
    '''
    AMBIGUITY_DETECTION = 'ambiguity-detection'
    ANSWER_SCORING = 'answer-scoring'
    CONTRADICTION_DETECTION = 'contradiction-detection'
    LETS_DISCUSS_CREATE = 'discuss/create'
    LETS_DISCUSS = 'discuss'
    LETS_DISCUSS_RETRIEVE = 'discuss/count'
    LETS_DISCUSS_DELETE = 'discuss/delete'
    DOCUMENTS_INGEST = 'documents/ingest'
    DOCUMENTS_DELETE = 'documents/delete'
    DOCUMENTS_SEARCH = 'documents/search'
    EMAIL_ANALYSIS = 'email-analysis'
    EMOTION_DETECTION = 'emotion-detection'
    FILE_CONVERTER = 'file-converter'
    FLASHCARD_GENERATION = 'flashcard-generation'
    INTENT_CLASSIFICATION = 'intent-classification'
    LANGUAGE_DETECTION = 'language-detection'
    LOGICAL_ERROR_DETECTION = 'logical-error-detection'
    MICROLESSON = 'microlesson'
    NER = 'ner'
    PARAPHRASE = 'paraphrase'
    PROFANITY = 'profanity'
    QUESTION_AND_ANSWER_GENERATION = 'qna-generation'
    QUESTION_ANSWERING = "question-answering"
    REVIEW_TAGGER = 'review-tagger'
    SEARCH_RECOMMENDATION = 'search-recommendations'
    SENTIMENT_ANALYSIS = 'sentiment-analysis'
    SIMPLIFY = 'simplify'
    STRING_SIMILARITY = 'string-similarity'
    SUMMARIZATION = 'summarization'
    TABLE_GENERATOR = 'table-generator'
    TAG_GENERATION = 'tag'
    TRANSCRIPTION_CORRECTION = 'transcript-correction'
    BATCH_SERVICE = 'batch-service2'

