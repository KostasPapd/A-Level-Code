def recordClass():
    class Records:
        def __init__(self, gfirst, glast, gid, gdob):
            self.name = gfirst+" "+glast
            self.id = gid
            self.dob = gdob


    students = []
    firstname = ["Kostas", "Ali", "Lewis"]
    lastname = ["Papadopoulos", "Haider", "Read"]
    studentnum = ["B32908", "B34331", "B54612"]
    DoB = ["01/06/2007", "02/01/2005", "15/12/2006"]

    for i in range(len(firstname)):
        students.append(Records(firstname[i], lastname[i], studentnum[i], DoB[i]))
        print(f"Name: {students[i].name}, ID Number: {students[i].id}, Date of Birth: {students[i].dob}")

if __name__ == "__main__":
    recordClass()
