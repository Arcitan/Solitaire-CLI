# import dependencies
from src.CardStack import CardStack
from src.Card import SUITS_SYMBOLS


class Foundation(CardStack):
    """
    A class that represents a Foundation on the Solitaire board.
    """
    def __init__(self, suit):
        """
        Constructor for a foundation stack.
        :param suit: The type of suit this foundation is for.
        """
        super().__init__()
        self.suit = suit

    def is_full(self):
        """
        Checks if the foundation is full.
        :return: True if it is, False otherwise.
        """
        return len(self) == 13

    def add_card(self, card):
        """
        Adds a card to the foundation, if it's valid to do so.
        :param card: A CardSequence object.
        :return: True if successful, False otherwise.
        """
        if card.cards[0].suit == self.suit and card.cards[0].value > self.peek_top().value:
            self.cards.append(card)
            return True
        else:
            print(f"Cannot add {card} to the {self.suit} foundation.")
            return False

    def __repr__(self):
        """
        Constructs the string representation of the foundation.
        :return: The string representation.
        """
        if len(self) > 1:
            return "[[" + str(self.peek_top())
        elif len(self):
            return str(self.peek_top())
        else:
            return f"({SUITS_SYMBOLS['black'][self.suit]})"
