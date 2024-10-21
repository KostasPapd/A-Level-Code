l = [16, 3, 56, 23, 12, 43, 24, 78, 31]

def search(c, l):
      num = l[0]
      if c == 1:
            for i in range(0, len(l)-1):
                  if l[i] < num:
                        num = l[i]
            return num
      elif c == 2:
            for i in range(0, len(l)-1):
                  if l[i] > num:
                        num = l[i]
            return num
      else:
            print("Invalid choice")
            main(l)

def main(l):
      print("1. Search for smallest\n"
            "2. Search for largest")
      choice = int(input("Enter choice: "))
      number = search(choice, l)

      if choice == 1:
            print("Smallest number in the list is", number)
      else:
            print("Largest number in the list is", number)

main(l)
