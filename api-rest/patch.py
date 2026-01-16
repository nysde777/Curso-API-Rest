import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "email": "parcial@yopmail.com"
}

response = requests.patch(url, json=payload)

print(response.status_code)
print(response.json())
