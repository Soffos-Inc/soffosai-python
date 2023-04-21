from .service_io import ServiceIO
from ..constants import Services


class TableGeneratorIO(ServiceIO):
    service = Services.TABLE_GENERATOR
    required_input_fields = ["table_format", "text"]
    input_structure = {
        "table_format": str, # markdown or CSV
        "text": str
    }
    output_structure = {
    "tables": [
            {
                "title": str,
                "table": str,
                "note": str
            },
        ]
    }
