import random

class Card(object):
    suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_name = [None, 'Ace', '2', '3', '4', '5', '6', 
                    '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_name[self.rank], Card.suit_name[self.suit])

    def __cmp__(self, other):       #method compare 2 la bai c1, c2
        c1 = self.suit, self.rank
        c2 = other.suit, other.rank
        return cmp(c1, c2)


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i = 0):     #chia bai tu la tren top cua deck
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        # self.label = label


def main():
    c1 = Card(3, 12)
    c2 = Card(3, 5)
    print c1, c2, c1 > c2

    deck = Deck()
    deck.shuffle()

    hand = Hand()
    deck.move_card(hand, 5)
    print deck
    print ''
    print hand

if __name__ == '__main__':
    main()