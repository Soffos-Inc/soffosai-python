from soffos import Client
from soffos.common.constants import Services
from soffos.common.constants import SOFFOS_SERVICE_URL
import http3
import requests

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

ai_client = Client(api_key)


url = SOFFOS_SERVICE_URL + "file-converter/"
headers = {
    "x-api-key": api_key,
    "Content-Type": "multipart/form-data"
}
data = {
    'user': "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    'file': open('Epidemiology.docx', 'rb')
}

# files = {'file': open('Epidemiology.docx', 'rb')}

response = requests.post(url, headers=headers, data=data)

print(response)
