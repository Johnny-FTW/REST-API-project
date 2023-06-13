import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={"product_id":"hiii"})

# print(response.text)
print(response.json())
# print(response.status_code)