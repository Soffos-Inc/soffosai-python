import json
from soffosai.core.pipelines import Pipeline
from soffosai.core.nodes import FileConverterNode, DocumentsIngestNode, QuestionAnsweringNode

# a helper function to get the filename provided the file is in the same directory
def get_filename(full_file_name:str):
    return full_file_name.split(".")[0]


# a helper function that puts the document_id inside a list. Useful when the source node's output is
# document_id and the current node needs document_ids
def put_docid_inside_list(doc_id):
    return [doc_id]

# initialize the generic Pipeling
my_pipe = Pipeline(
    # define your nodes in order of execution
    nodes = [
        # This node's name is fileconv for reference of other nodes. It needs the argument file to come from user input 'file'
        FileConverterNode(name="fileconv", file=("user_input", "file")), 
        DocumentsIngestNode(
            name = 'ingest', 
            document_name=("user_input", (get_filename, "file")), # this argument needs the return value of get_filename(user_input['file'])
            text=("fileconv", "text") # this node needs its text argument to come from fileconv output field named 'text'
        ),
        QuestionAnsweringNode(
            name="qa",
            question=("user_input", "question"), 
            document_ids=("ingest", (put_docid_inside_list, "document_id"))# this argument needs the return value of put_docid_inside_list(<output of ingest node with key 'document_id'>)
        )
    ]
)

src = {
    "user": "client_id", 
    "file": "matrix.pdf",
    "question": "who is Neo?"
}
output = my_pipe.run(user_input=src)
print(json.dumps(output, indent=4))
