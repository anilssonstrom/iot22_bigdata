import json
import requests
from pprint import pprint

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response.status_code)
# print(type(response.text))
# print(response.text)

todos = json.loads(response.text)
# print(type(todos))
# pprint(todos[:3], width=1, indent=4)

print("Antal Todos:", len(todos))

number_completed = 0
for todo in todos:
    if todo['completed']:
        number_completed += 1

print("Klara todos: ", number_completed)

"""{
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
}"""
