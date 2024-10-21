import json

def format(a):
    print("Convert Python dictionary into JSON formatted String")
    d = json.dumps(a)
    print(d)
    return d

def dict(a):
    print("Started converting JSON string document to Python dictionary")
    developerDict = json.loads(a)
    print(developerDict)
    return developerDict

list = [
    {
        'name': "Kostas Papadopoulos",
        'languages': ["Python", "HTML"]
    },
    {
        'name': "John White",
        'languages': ["Python", "Javascript", "C++"]
    }
]

with open("sample.json", "w") as file:
    json.dump(list, file)

f = open("sample.json", "r")
print(f.read())
f.close()

g = {'name': ["Kostas Papadopoulos", "John White"], 'languages': [["Python", "HTML"], ["Python", "Javascript", "C++"]]}

#array = format(list)
#q = dict(array)
#print(g['name'])
#print(g["languages"])
