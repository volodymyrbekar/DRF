import requests


# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anythoing"

get_response = requests.get(endpoint, json={"query": "Hello world"})  # API -> Method
# print(get_response.text)

print(get_response.json())
print(get_response.status_code)



