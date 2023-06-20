import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'some title for creating api view',
    'price': 42.95
}


get_response = requests.post(endpoint, json=data)

print(get_response.json())

