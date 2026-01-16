import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.status_code)

data = response.json()
print(response.headers)
print(data)