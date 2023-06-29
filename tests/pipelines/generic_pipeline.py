import json
from soffosai.core import Pipeline
from soffosai.core import NodeConfig
from soffosai.common.constants import ServiceString


src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix",
    "question": "who is Neo?"
}

file_converter_node = NodeConfig(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file")
    }
)

document_ingest_node = NodeConfig(
    service=ServiceString.DOCUMENTS_INGEST,
    source={
        "name": (0, "name"),
        "text": (1, "text")
    }
)

question_answering_node = NodeConfig(
    service=ServiceString.QUESTION_ANSWERING,
    source={
        "document_ids": (2, "document_id"),
        "question": (0, "question")
    }
)


my_pipe = Pipeline(
    stages = [file_converter_node, document_ingest_node, question_answering_node]
)
print(json.dumps(my_pipe.run(user_input=src), indent=4))