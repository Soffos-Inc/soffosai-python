import soffosai
from soffosai.core.pipelines import Pipeline
from soffosai.core.nodes import Node
from soffosai.common.constants import ServiceString


src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix"
}
file_converter_node = Node(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file")
    }
)

document_ingest_node = Node(
    service=ServiceString.DOCUMENTS_INGEST,
    source={
        "name": (0, "name"),
        "text": (1, "text")
    }
)

question_answering_node = Node(
    service=ServiceString.QUESTION_ANSWERING,
    source={
        "document_ids": (2, "document_id"),
        "message": "Who is Neo?"
    }
)

my_pipe = Pipeline(
    stages = [file_converter_node, document_ingest_node, question_answering_node],
    user = 'franco',
    source = src
)

print(my_pipe.run()[3])
