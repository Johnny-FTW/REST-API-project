import requests



endpoint = "http://localhost:8000/api/products/16549841981981/"

response = requests.get(endpoint)


print(response.json())