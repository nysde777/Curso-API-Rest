import requests
url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Content-Type": "application/json", 
    "Accepet": "application/json"
}

payload = {
    "name": "Ana Martinez",
    "email": "ana@yahoo.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())