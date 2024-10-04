import json

data = {'Name': "Md Aftab", "Age": 20, "Marks": 85}
s = json.dumps(data)
print(s)

# Access The Value Of Age From Given Json Data
data = {'Name': "Md Aftab", "Age": 20, "Marks": 85}
sb = json.loads(s)
print(sb["Age"])

# Pretty Print Of JSON Data
s = json.dumps(data, indent=4, separators=(",", ": "))
print(s)

print(type(data))

