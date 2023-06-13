import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title": "hii" })


print(response.json())
