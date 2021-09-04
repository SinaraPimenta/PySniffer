import json

# some JSON:
MYJSON = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(MYJSON)

# the result is a Python dictionary:
print(y["age"])
