from .service_io import ServiceIO
from ..constants import Services


class LetsDiscussCreateIO(ServiceIO):
    service = Services.LETS_DISCUSS_CREATE
    required_input_fields = ["context"]
    input_structure = {
        "context": str
    }
    output_structure = {
        "session_id": str
    }


class LetsDiscussIO(ServiceIO):
    service = Services.LETS_DISCUSS
    required_input_fields = ["session_id", "query"]
    input_structure = {
        "session_id": str,
        "query": str
    }
    output_structure = {
        "response": str,
        "context": str,
        "messages": [
            {
            "text": str,
            "source": str # "user" or "soffos"
            },
        ]
    }


class LetsDiscussRetrieveIO(ServiceIO):
    service = Services.LETS_DISCUSS_RETRIEVE
    required_input_fields = ["return_messages"]
    input_structure = {
        "return_messages": bool
    }
    output_structure = {
        "sessions": [
            {
            "context": str,
            "session_id": str,
            "messages": [
                {
                "query": str,
                "response": str,
                "message_id": int
                },
                {
                "query": str,
                "response": str,
                "message_id": int
                },
            ]
            }
        ],

        "session_count": int
    }


class LetsDiscussDeleteIO(ServiceIO):
    service = Services.LETS_DISCUSS_DELETE
    required_input_fields = ["session_ids"]
    input_structure = {
        "session_ids": str
    }
    output_structure = {
        "success": bool
    }
