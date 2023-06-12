from .service_io import ServiceIO
from ..constants import ServiceString


class AnswerScoringIO(ServiceIO):
    service = ServiceString.ANSWER_SCORING
    required_input_fields = ["context", "question", "user_answer"]
    optional_input_fields = ["answer"]
    input_structure = {
        "context": str,
        "answer": str,
        "user_answer": str
    }
    # output_fields = ["score", "reasoning"]
    output_structure = {
        "score": float,
        "reasoning": str
    }
 