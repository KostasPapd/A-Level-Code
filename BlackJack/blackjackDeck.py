import random
from BlackJack.blackjackCards import PlayingCard

class Deck:
    def __init__(self):
        self.__cards = []

        #creates deck
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for i in range(4):
            for j in range(13):
                newCard = PlayingCard(suits[i], ranks[j], values[j])
                self.__cards.append(newCard)

#change to generate a position and then generate the card and put in that position
    def shuffle(self):
        cardNum = []
        while len(cardNum) < 52:
            num = random.randint(0, 51)
            while num in cardNum:
                num = random.randint(0, 51)
            cardNum.append(num)


if __name__ == "__main__":
    myDeck = Deck()
    myDeck.shuffle()