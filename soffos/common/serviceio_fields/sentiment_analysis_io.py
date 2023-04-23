from .service_io import ServiceIO
from ..constants import Services


class SentimentAnalysisIO(ServiceIO):
    service = Services.SENTIMENT_ANALYSIS
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split", "sentence_overlap"]
    input_structure = {
        "text": str, 
        "sentence_split": int,
        "sentence_overlap": bool
    }
    output_structure = {
        "sentiment_breakdown": [
            {
                "text": str,
                "start": int,
                "end": int,
                "sentiment": {
                    "negative": float,
                    "neutral": float,
                    "positive": float
                }
            },
        ],
        "sentiment_overall": {
            "negative": float,
            "neutral": float,
            "positive": float
        }
    }
