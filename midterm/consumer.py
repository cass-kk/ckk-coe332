import requests
import json

response = requests.get(url="http://localhost:5003/animals")

print(response.status_code)
print(response.json())
print(response.headers)
