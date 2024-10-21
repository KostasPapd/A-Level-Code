class Player:
    def __init__(self, name):
        self.__name = name
        self.__score = 0


if __name__ == "__main__":
    name = input("Enter your name: ")
    gamePlayer = Player(name)