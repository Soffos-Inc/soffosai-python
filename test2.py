import requests

url = "http://localhost:8000/service/file-converter/"

payload = {'user': 'b5601df8-6af3-4c1a-9ded-b7df4c506eab'}
files=[
  ('file',('matrix.pdf',open('C:/Users/Administrator/Downloads/matrix.pdf','rb'),'application/pdf'))
]
headers = {
  'x-api-key': 'Token 3465f9a9-dcf9-4cf9-851e-f8cbb1f275b4'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
