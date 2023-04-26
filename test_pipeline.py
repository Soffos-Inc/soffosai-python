import json
from soffos.client.soffos import Client, Services
from soffos.pipeline import SoffosPipeline

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

sources = {
    "name": "Epidemiology",
    "file": "Epidemiology.docx",
    "message": "What is the document all about?"
}
my_pipeline = SoffosPipeline(
    apikey=api_key,
    user="b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    stages=[Services.FILE_CONVERTER, Services.DOCUMENTS_INGEST, Services.QUESTION_ANSWERING],
    sources=sources
)

response = my_pipeline.run()
print(json.dumps(response, indent=4))
