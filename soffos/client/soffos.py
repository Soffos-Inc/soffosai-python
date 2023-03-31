'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-03-23
Purpose: The main module of Soffos
-----------------------------------------------------
'''

import requests

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
    Contains the list of Soffos services assigned as attributes for better coding experience
    '''
    
    AMBIGUITY_DETECTION = 'ambiguity-detection'
    ANSWER_SCORING = 'answer-scoring'
    CONTRADICTION_DETECTION = 'contradiction-detection'
    LETS_DISCUSS = 'discuss'
    DOCUMENTS_INGEST = 'documents/ingest'
    EMAIL_ANALYSIS = 'email-analysis'
    EMOTION_DETECTION = 'emotion-detection'
    FILE_CONVERTER = 'file-converter'
    FLASHCARD_GENERATION = 'flashcard-generation'
    INTENT_CLASSIFICATION = 'intent-classification'
    LANGUAGE_DETECTION = 'language-detection'
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
    TAG_GENERATION = 'tag'
    TRANSCRIPTION_CORRECTION = 'transcript-correction'
    BATCH_SERVICE = 'batch-service2'


class Client:

    def __init__(self, apikey) -> dict:

        self._apikey = apikey
        # self.service = None
        self.headers = {
            "x-api-key": apikey,
            "content-type": "application/json"
        }
        self._input = None
        self._question = None
        self._answer = None
        self._tags = None
        self._knowledge = None

    @property
    def service(self):
        return self._service


    @service.setter
    def service(self, value):
        if value not in SERVICES_LIST:
            raise KeyError(f"Invalid Service please choose from {SERVICES_LIST} or import Services for faster coding")

        self._service = value


    @property
    def input(self):
        return self._input


    @input.setter
    def input(self, value):
        self._input = value


    @property
    def question(self):
        return self._question


    @question.setter
    def question(self, value):
        self._question = value
        self._input = value


    @property
    def knowledge(self):
        return self._knowledge


    @knowledge.setter
    def knowledge(self, value):
        self._knowledge = value


    def get_response(self):
        response = requests.post(
            url=SOFFOS_SERVICE_URL + self.service + "/",
            headers=self.headers,
            json={
                "user": self._apikey,
                "message": self.question,
                "document_text": self.knowledge
            }
        )
        return response.json()