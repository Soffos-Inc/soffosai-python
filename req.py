import requests
import mimetypes

url = "https://dev-api.soffos.ai/service/file-converter/"

payload={'user': 'b5601df8-6af3-4c1a-9ded-b7df4c506eab'}
filename = 'Epidemiology.docx'
file = open('Epidemiology.docx','rb')
mime_type, _ = mimetypes.guess_type(filename)
print(mime_type)
files={
  'file':('Epidemiology.docx', file, mime_type)
}
headers = {
  'x-api-key': 'Token d75d8745-c0c7-426c-b849-c6c48ad9b3ed'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
file.close()
