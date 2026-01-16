import requests

url = "https://jsonplaceholder.typicode.com/users"

payload = {
    "name": "Juan", 
    "email": "juan@gmail.com"
}

response = requests.post(url, json=payload)

print(response.status_code)

print(response.json())

