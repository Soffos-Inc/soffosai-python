import json
from soffos.client.http_client import Client, Services
from soffos.pipeline import SoffosPipeline
from apikey import api_key


sources = {
    "name": "Epidemiology",
    "file": "Epidemiology.docx",
    "message": "What is the document all about?"
}
my_pipeline = SoffosPipeline(
    apikey=api_key,
    user="b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    stages=[Services.FILE_CONVERTER, Services.DOCUMENTS_INGEST, Services.QUESTION_ANSWERING],
    sources=sources,
)

response = my_pipeline.run()
with open("output.txt", "w", encoding="utf-8") as target:
    target.writelines(json.dumps(response, indent=4))

##############################################################################################

import os
import requests
import json
import mimetypes
from apikey import api_key

# prepare the data
headers = {
    'x-api-key': api_key
}

data = {
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    "normalize": 0
}

file_loc = "Epidemiology.docx"
filename = str(os.path.basename(file_loc))
mime_type, _ = mimetypes.guess_type(file_loc)

with open(file_loc, 'rb') as file:
    files = {
        "file": (filename, file, mime_type)
    }
    file_converter_response = requests.post(
        url = "https://dev-api.soffos.ai/service/file-converter/",
        headers = headers,
        data = data,
        files = files
    )

print(file_converter_response.json())

# # document ingest stage:
# headers = {
#     'x-api-key': api_key,
#     "Content-Type": "application/json"
# }
# _json = {
#   "name": "Epidemiology",
#   "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
#   "text": file_converter_response.json()["text"]
# }

# document_ingest_response = requests.post(
#     url = "https://dev-api.soffos.ai/service/documents/ingest/",
#     headers = headers,
#     json = _json,
# )

# # Question Answering Stage

# _json = {
#     "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
#     "message": "How can Soffos help me build amazing applications?",
#     "document_ids": [
#         'e9f46bf7650743fc86a8a8aee2dffdfc',
#     ],
#     "check ambiguity": True,
#     "check_query_type": True,
#     "generic_response": False,
# }

# response = requests.post(
#     url = "https://dev-api.soffos.ai/service/question-answering/",
#     headers=headers,
#     json = _json
# )

# print(response.json())
