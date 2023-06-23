import requests


headers = {'Authorization': 'Bearer 56b7e8de71149f75c278fddf25116951b0009f11'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "DONE",
    "price": 32.99
}

response = requests.post(endpoint, json=data, headers=headers)


print(response.json())