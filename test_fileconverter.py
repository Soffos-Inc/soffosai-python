from soffos import Client, Services
from apikey import api_key


ai_client = Client(api_key)

ai_client.user = "b5601df8-6af3-4c1a-9ded-b7df4c506eab"
ai_client.service = Services.FILE_CONVERTER
ai_client.src = 'Epidemiology.docx'
response = ai_client.get_response()
print(response.response)


# print(response.raw_response)