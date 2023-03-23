import json
import requests
from pprint import pprint

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response.status_code)
print(type(response.text))
# print(response.text)

todos = json.loads(response.text)
print(type(todos))
#pprint(todos[:3], width=1, indent=4)
print(len(todos))
