from petsConstructor import *

dogList = []
dogSpec = ["German shepherd", "Golden Retriever", "Chocolate Labrador"]
dnames = ["Indy", "Simba", "Chockie"]
dprice = [450.0, 350.0, 200.0]
dages = [1, 2, 7]
dwords = ["dog", "dog one", "dog two"]
dsniff = ["sock", "food", "bottle"]

for n in range(len(dnames)):
    dogList.append(Dog(dogSpec[n], dnames[n], dages[n]))
    dogList[n].set_price(dprice[n])
    print(f"{dogList[n].description()}, Species: {dogSpec[n]}, Price: {dogList[n].get_price()}")
    print(dogList[n].speak(dwords[n]))
    dogList[n].sniff(dsniff[n])
    print()

catList = []
catBre = ["Black and white", "Tabby"]
cnames = ["Domino", "Willow"]
cwords = ["cat", "cat 1"]
cprice = [250.0, 300.0]
cages = [3, 4]

for n in range(len(cnames)):
    catList.append(Cat(catBre[n], cnames[n], cages[n]))
    catList[n].set_price(cprice[n])
    print(f"{catList[n].description()}, Breed: {catBre[n]}, Price: {catList[n].get_price()}")
    catList[n].sleep()
    catList[n].meow()
    print(catList[n].speak(cwords[n]))
    print()
