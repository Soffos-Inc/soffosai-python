from .service_io import ServiceIO
from ..constants import ServiceString


class DocumentsIngestIO(ServiceIO):
    service = ServiceString.DOCUMENTS_INGEST
    required_input_fields = ["document_name", ]
    require_one_of_choice = [["text", "tagged_elements"]]
    defaults = ["text"]
    optional_input_fields = ["meta"]
    input_structure = {
        "document_name": str,
        "meta": dict,
        "text": str,
        "tagged_elements": [dict, dict]
    }
    # output_fields = ["success", "document_id"]
    output_structure = {
        "success": bool,
        "document_id": str
    }
    primary_output_field = "document_id"


class DocumentSearchIO(ServiceIO):
    service = ServiceString.DOCUMENTS_SEARCH
    required_input_fields = []
    require_one_of_choice = []
    defaults = ["query"]
    optional_input_fields = [
        "query", "filters", "document_ids", "top_n_keywords", 
        "top_n_natural_language", "date_from", "date_until"
    ]
    input_structure = {
        "query": str,
        "document_ids": list,
        "top_n_keyword": int,
        "top_n_natural_language": int,
        "filters": dict,
        "date_from": str,
        "date_until": str
    }
    # output_fields = ["passages"]
    output_structure = {
        "passages": [{
            "content": str,
            "document_id": str,
            "created_at": str,
            "name": str,
            "scores": [
                {
                    "keyword": float,
                    "semantic": float
                },
            ],
            "meta": {}
        },],
        
        "text": str
    }

    @classmethod
    def special_validation(self, payload:dict):
        payload_keys = payload.keys()
        # if 'query' not in payload_keys and 'filters' not in payload_keys:
        #     return False, "If query is not provided, please provide 'filters' argument."
        
        if 'top_n_natural_language' in payload_keys:
            if payload['top_n_natural_language'] > 0 and 'query' not in payload_keys and 'document_ids' not in payload_keys:
                return False, "If document_ids are not defined: query is required if top_n_natural_language is defined and is greater than 0."

        return super().special_validation(payload)


class DocumentDeleteIO(ServiceIO):
    service = ServiceString.DOCUMENTS_DELETE
    required_input_fields = ["document_ids"]
    input_structure = {
        "document_ids": [str, str]
    }
    output_structure = {
        "success": bool
    }
