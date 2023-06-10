import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/"

response = requests.get(endpoint, data={"query":"Hello world"})

# print(response.text)
print(response.status_code)