'''
Organization of constant lists and dictionaries
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
    LETS_DISCUSS = 'discuss'
    DOCUMENTS_INGEST = 'documents/ingest'
    DOCUMENTS_DELETE = 'documents/delete'
    DOCUMENTS_SEARCH = 'documents/search'
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

