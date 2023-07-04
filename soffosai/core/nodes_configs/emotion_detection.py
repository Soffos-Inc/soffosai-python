from .node import NodeConfig
from soffosai.core.services import EmotionDetectionService, inspect_arguments


_EMOTION_LIST = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation"]

class EmotionDetectionNodeConfig(NodeConfig):
    '''
    Emotion Detection configuration for Pipeline Use
    '''
    def __init__(self, text:str, sentence_split:int=4, sentence_overlap:bool=False, emotion_choices:list=_EMOTION_LIST):
        for emotion in emotion_choices:
            if emotion not in _EMOTION_LIST:
                raise ValueError(f"{emotion} is not valid as an emotion_choices element. Please choose from {_EMOTION_LIST}.")
        source = inspect_arguments(self.__call__, text, sentence_split, sentence_overlap, emotion_choices)
        service = EmotionDetectionService
        super().__init__(service, source)
