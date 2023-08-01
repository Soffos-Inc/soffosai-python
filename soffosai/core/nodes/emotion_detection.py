from .node import Node
from soffosai.core.services import EmotionDetectionService, inspect_arguments

_EMOTION_LIST = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation"]

class EmotionDetectionNode(Node):
    '''
    Emotion Detection configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, sentence_split:int=4, sentence_overlap:bool=False, emotion_choices:list=_EMOTION_LIST):
        source = inspect_arguments(self.__init__, name, text, sentence_split, sentence_overlap, emotion_choices)
        service = EmotionDetectionService
        super().__init__(name, service, source)
