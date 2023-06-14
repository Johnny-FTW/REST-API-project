import requests



endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "AJAJAJ",
    "price": 20.99
}


response = requests.put(endpoint, json=data)
print(response.json())