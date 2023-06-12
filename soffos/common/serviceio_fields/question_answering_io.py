from .service_io import ServiceIO
from ..constants import ServiceString


class QuestionAnsweringIO(ServiceIO):
    service = ServiceString.QUESTION_ANSWERING
    required_input_fields = ["message"]
    require_one_of_choice = [["document_text", "document_ids"]]
    defaults = ["document_text"]
    optional_input_fields = ["check_ambiguity", "check_query_type", "generic_responses"]
    input_structure = {
        "message": str,
        "document_ids": [
            str,
            str
        ],
        "document_text": str, # should not be defined if document_ids field is present
        "check ambiguity": bool,
        "check_query_type": bool,
        "generic_response": bool,
        "meta": {
            "session_id": str
        }
    }
    output_structure = {
        "answer": str,
        "valid_query": bool,
        "no_answer": bool,
        "message_id": str,
        "context": str,
        "highlights": [
            {
                "span": [int, int],
                "sentence": str
            },
        ],
        "passages": [dict, dict]
    }
