import random

class Deck:
    def __init__(self, number = 1):
        self.number = number
        self.cards = []

    def generate(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queeen", "King"]

        for x in range(self.number):
            for suit in suits:
                for value in values:
                    card = str(value) + " of " + suit
                    self.cards.append(card)

    def shuffle(self):
        for x in range(100000):
            pos = random.randint(0, len(self.cards)-1)
            card = self.cards.pop(pos)
            self.cards.append(card)

    def deal(self, number):
        cards = []
        for x in range(number):
            card = self.cards.pop()
            cards.append(card)
        return cards

    def reset(self):
        self.cards = []

#class Player:



deck = Deck(4)
deck.generate()
deck.shuffle()

print(deck.cards)
print(deck.deal(8))
print(len(deck.cards))

deck.reset()
print(deck.cards)
