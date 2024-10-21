square = [[0, 1, 2, 3, 4, 5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]


def display(square):
    for row in range(0, 7):
        for column in range(0, 6):
            print(square[row][column], "    ", end='')  # prints Horizontally
        print()  # adds New Line
    main(square)

def deCipher(cryptogram):
    cryptogram = cryptogram.replace(" ", "")  # remove spaces
    word = ""  # initialise the value of word to empty string
    for n in range(0, len(cryptogram), 3):
        r = cryptogram[n]
        c = cryptogram[n + 1]
        letter = square[int(r)][int(c)]
        word = word + letter
    return word

def main(square):
    print("1. Display board\n"
          "2. Decipher message")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display(square)
    elif choice == 2:
        code = input(" Enter Cryptogram (the ciphered message) ...  ")
        print("The Secret word is ... " + deCipher(code))



main(square)
