class Card:
    def __init__(self, value):
        self.value = value
        suit_number = value.split()
        self.suit = suit_number[1]
        if suit_number[0] == "A":
            self.number = 14
        elif suit_number[0] == "K":
            self.number = 13
        elif suit_number[0] == "Q":
            self.number = 12
        elif suit_number[0] == "J":
            self.number = 11
        else:
            self.number = int(suit_number[0])

    def suit(self):
        return self.suit

    def number(self):
        return self.number


class Hand:
    cards = []
    cards_numbers = []

    def add_card(self, card):
        self.cards.append(card)
        self.cards_numbers.append(card.number())

    def sort(self):
        self.cards.sort(key=Card.number)
        self.cards_numbers.sort()

    def value(self):
        suits = {"H": 0, "D": 0, "C": 0, "S": 0}

        for card in self.cards:
            suits[card.suit] += 1

        for suit in suits:
            # all the same suit
            if suits[suit] == 5:
                # sequential
                for n in range(1, 5):
                    # flush
                    if self.cards_numbers[n] - self.cards_numbers[n - 1] > 1:
                        return 6
                # royal flush
                if self.cards_numbers is [10, 11, 12, 13, 14]:
                    return 10
                # straight flush
                else:
                    return 9

