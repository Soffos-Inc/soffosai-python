from .service_io import ServiceIO
from ..constants import Services


class EmailAnalysisIO(ServiceIO):
    service = Services.EMAIL_ANALYSIS
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "analysis": {
            "keypoints": [str, str],
            "topics": [str, str],
            "sender": str,
            "receiver": [str, str],
            "mentions": [str, str],
            "sentiment": str,
            "urgency": str,
            "dates": [str, str]
        }
    }

