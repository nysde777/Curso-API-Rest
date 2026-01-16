import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(url)

print(response.status_code)