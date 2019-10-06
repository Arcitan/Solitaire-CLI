# import dependencies
from src.CardStack import CardStack


class CardSequence(CardStack):
    """
    A class that represents the face-up sequence of cards at the top of a Tableau. Primarily used to transfer cards
    to-and-between tableaus.
    Data definition is as follows:
        - A CardSequence is a card, attached to another CardSeq (based on rules of whether it's valid to attach).
        - A CardSequence is exactly one card.
    """
    def __init__(self, cards):
        """
        Constructor for a CardSequence.
        :param cards: A list of Card objects.
        """
        super().__init__()
        # Construct the CardSequence based on the data definition
        self.cards.append(cards.pop(0))
        for card in cards:
            if card.can_attach_to(self.peek_top()):
                self.cards.append(card)
            else:
                # Should never get here
                raise ValueError("The provided list of cards cannot form a valid CardSequence.")
