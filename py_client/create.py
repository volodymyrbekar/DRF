import requests


headers = {'Authorization': 'Bearer 587230e05b5e3c10823bf5b6eee025373b239550'}
endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'some title for creating api view',
    'price': 42.95
}


get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

