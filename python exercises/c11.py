import requests
import json

a = requests.get('https://jsonplaceholder.typicode.com/todos/50')
b = a.text
c = json.loads(b)

# print(c["title"])

d = requests.get('https://jsonplaceholder.typicode.com/users')
e = d.text
f = json.loads(e)

for item in f:
	name = item["name"]
	email = item["email"]
	
	address = item["address"]
	city = address["city"]

	print("{}, {}, {}".format(name, email, city))