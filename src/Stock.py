# import dependencies
import random
from src.CardStack import CardStack
from src.Card import Card


SUITS = ["spades", "hearts", "diamonds", "clubs"]
COLORS = ["white", "black"]
RANKS = ["A"] + list(map(str, range(2, 11))) + ["J", "K", "Q"]


class Stock(CardStack):
    """
    Class for the Stock. (Basically, the deck of face-down cards.)
    """
    def __init__(self):
        """
        Constructor for the stock. Initially contains all 52 cards face-down.
        """
        super().__init__()
        self.cards = [Card(color, rank, suit, True) for color in COLORS for rank in RANKS for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the order of the cards in-place.
        """
        random.shuffle(self.cards)

    def refill(self, cards):
        """
        Refills the stock with a set of cards.
        :param cards: A list of Card objects.
        """
        self.cards.extend(cards)

    def __repr__(self):
        """
        Constructs the string representation of the stock.
        :return: The string representation.
        """
        if len(self) > 1:
            return "[[[*]"
        elif len(self):
            return "[*]"
        else:
            return ""
