import json
from pprint import pprint


data = {
    "shopping": {
        "store": "ICA Maxi",
        "selfscan": True,
        "items": ["milk", "bread", "cookies", "pizza"],
        "expected_cost": 150
    }
}
"""
str_data = json.dumps(data, indent="\t")
print(str_data)
print(type(str_data))
"""
"""
#s = '{"shopping": {"store": "ICA Maxi", "selfscan": true, "items": ["milk", "bread", "cookies", "pizza"], "expected_cost": 150}}'
s = '[1, 2, 3, 4, {"a": 1, "b": 2}]'
my_data = json.loads(s)
print(my_data)
print(type(my_data))

#print(my_data['shopping']['store'])
"""

"""
with open("datafile.json", "w") as my_file:
    json.dump(data, my_file)

with open("datafile.json", "r") as my_file:
    file_data = json.load(my_file)
    pprint(file_data)
    print(type(file_data))
    # print(type(file_data['shopping']['expected_cost']))
"""

hand = (4, "Hearts")
json_str = json.dumps(hand)
py_obj = tuple(json.loads(json_str))

print(hand == py_obj)
print(type(hand))
print(type(py_obj))
print(hand)
print(py_obj)
