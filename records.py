from oopRecords import recordClass
def recordTuple():
    firstname = ["Kostas", "Ali", "Lewis"]
    lastname = ["Papadopoulos", "Haider", "Read"]
    studentnum = ["B32908", "B34331", "B54612"]
    DoB = ["01/06/2007", "02/01/2005", "15/12/2006"]

    table = []
    for i in range(len(firstname)):
        record = []
        record.append(firstname[i])
        record.append(lastname[i])
        record.append(studentnum[i])
        record.append(DoB[i])
        table.append(record)

    s = tuple(table)
    print(s)

def recordDictionary():
    students = [
        {"firstname": "Kostas", "lastname": "Papadopoulos", "studentnum": "B32908", "DoB": "01/06/2007"},
        {"firstname": "Ali", "lastname": "Haider", "studentnum": "B34331", "DoB": "02/01/2005"},
        {"firstname": "Lewis", "lastname": "Read", "studentnum": "B54612", "DoB": "15/12/2006"}
    ]
    for student in students:
        print("Name:", student["firstname"], student["lastname"]+","+" ID Number:", student["studentnum"]+","+
              " Date of Birth:", student["DoB"])


print("Tuple:")
recordTuple()
print()
print("Dictionary:")
recordDictionary()
print()
print("Class:")
recordClass()
