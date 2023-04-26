from .service_io import ServiceIO
from ..constants import Services


class DocumentsIngestIO(ServiceIO):
    service = Services.DOCUMENTS_INGEST
    required_input_fields = ["name", ]
    require_one_of_choice = [["tagged_elements", "text"]]
    optional_input_fields = ["meta"]
    input_structure = {
        "name": str,
        "meta": dict,
        "text": str
    }
    # output_fields = ["success", "document_id"]
    output_structure = {
        "success": bool,
        "document_id": str
    }

class DocumentSearchIO(ServiceIO):
    service = Services.DOCUMENTS_SEARCH
    required_input_fields = []
    require_one_of_choice = [["query", "filters", "document_ids"]]
    optional_input_fields = [
        "query", "filters", "document_ids", "top_n_keywords", 
        "top_n_natural_language", "date_from", "date_until"
    ]
    input_structure = {
        "query": str,
        "document_ids": str,
        "top_n_keyword": int,
        "top_n_natural_language": int,
        "filters": dict,
        "date_from": str,
        "date_until": str
    }
    # output_fields = ["passages"]
    output_structure = {
        "passages": {
            "content": str,
            "document_id": str,
            "created_at": str,
            "name": str,
            "scores": [
                {
                    "keyword": float
                },
            ],
            "meta": {}
        }
    }


class DocumentDeleteIO(ServiceIO):
    service = Services.DOCUMENTS_DELETE
    required_input_fields = ["document_ids"]
    input_structure = {
        "document_ids": [str, str]
    }
    output_structure = {
        "success": bool
    }
