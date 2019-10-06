# import dependencies
from src.CardStack import CardStack


class Waste(CardStack):
    """
    A class that represents the waste stack on the Solitaire board.
    """
    def __init__(self):
        """
        Constructor for the waste stack.
        """
        super().__init__()

    def add_card(self, card):
        """
        Adds a card face-up to the waste stack.
        :param card: A Card object.
        """
        self.cards.append(card.flip_up())

    def __repr__(self):
        """
        Constructs the string representation of the waste.
        :return: The string representation.
        """
        if len(self) > 1:
            return "[[" + str(self.peek_top())
        elif len(self):
            return str(self.peek_top())
        else:
            return ""

