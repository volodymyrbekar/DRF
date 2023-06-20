import requests

products_id = input("What is product id you want to use? \n")
try:
    products_id = int(products_id)
except:
    products_id = None
    print(f'{products_id} not a valid id')

if products_id:
    endpoint = f"http://localhost:8000/api/products/{products_id}/delete/"

    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)

