from .service_io import ServiceIO
from ..constants import Services

class QuestionAndAnswerGenerationIO(ServiceIO):
    service = Services.QUESTION_AND_ANSWER_GENERATION
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split", "sentence_overlap"]
    input_structure = {
        "text": str,
        "sentence_split": int,
        "sentence_overlap": bool
    }
    output_structure = {
        "qna_list": [
            {
                "question": str,
                "answer": str,
                "chunk_index": int
            },
        ],

        "chunks": [
            {
                "text": str,
                "span_start": int,
                "span_end": int,
                "index": int
            },
        ]
    }
