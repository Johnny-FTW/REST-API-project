import requests



endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "DONE"
}

response = requests.post(endpoint, json=data)


print(response.json())