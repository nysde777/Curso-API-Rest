import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.options(url)

print(response.headers)