import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.head(url)

print(response.headers)