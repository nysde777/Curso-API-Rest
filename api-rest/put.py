import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "name": "Juanito Perez",
    "email": "juanito@yopmail.com"
}

response = requests.put(url, json=payload)

print(response.status_code)
print(response.json())