def lengthcheck(word, length, option):
    # word is the word to be checked
    # length is the length and
    # option 1: checking fixed length = l
    if option ==1:
        if len(word)== length:
            return True
        else:
            return False

    # option 2 checking if the word has length not shorter than lentgh

    elif option == 2:
        if len(word) >= length:
            return True
        else:
            return False

    # option 3 checking if the word has length not longer than length

    elif option == 3:
        if len(word)<= length:
            return True
        else:
            return False

def rangeCheck(num, minimum, maximum):
    if num >= minimum and num <= maximum:
        return True
    else:
        return False

def mobileNumCheck(number):
    numLen = str(number)
    if len(numLen) == 11:
        return True
    else:
        return False

def driversCheck(name, surname, gender, licenseNum): # https: // winterville.co.uk / uk - driving - licence - explained /
    pass

if __name__ == "__main__":
    print(lengthcheck("Kostas", 10, 3))
    print(rangeCheck(120, 3, 120))
    print(mobileNumCheck(10284786839))
    #print(driversCheck("Kostas", "Papadopoulos", "Male", 34))
