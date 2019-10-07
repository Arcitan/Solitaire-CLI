# import dependencies
from src.CardStack import CardStack


class Tableau(CardStack):
    """
    A class that represents a tableau on the Solitaire board.
    """
    def __init__(self, cards):
        """
        Constructor for the tableau.
        :param cards: A list of face-down Card objects.
        """
        super().__init__()
        self.unflipped = cards.copy()
        self.cards.append(self.unflipped.pop().flip_up())
        self.flipped = self.cards   # let flipped point to cards, so the peek/deal methods work only on flipped cards

    def add_card_sequence(self, card_seq):
        """
        Adds a sequence of cards to the top of the tableau, if it's valid to be added.
        :param card_seq: A CardSequence object.
        :return: True if successful, False otherwise.
        """
        # If the Tableau is empty, only a King can be added
        if self.is_empty() and card_seq.peek_bottom().rank == "K":
            self.flipped.extend(card_seq.cards)
            return True
        # Otherwise, only add if it's valid to attach the CardSeq to the top of the flipped cards
        elif card_seq.peek_bottom().can_attach_to(self.peek_top()):
            self.flipped.extend(card_seq.cards)
            return True
        else:
            print("The provided CardSequence cannot be added.")
            return False

    def deal(self, num=1, face_up=True):
        """
        Returns all the face-up cards, removes them from the stack, then flips over the first unflipped card.
        Overrides from CardStack.
        :param num: The number of cards to peek at. Default is 1.
        :param face_up: Whether the cards are dealt face-up or face-down. Default is True (i.e. face-up).
        :return: If num > 1, returns a list of the top *num* cards. Otherwise, just returns a single Card object.
        """
        if self.is_empty():
            return print("Cannot deal from an empty stack.")
        if face_up:
            removed = list(reversed([self.cards.pop().flip_up() for _ in range(num)]))
            if self.unflipped:
                self.flipped.append(self.unflipped.pop().flip_up())
            return removed
        else:
            removed = list(reversed([self.cards.pop().flip_down() for _ in range(num)]))
            if self.unflipped:
                self.flipped.append(self.unflipped.pop().flip_up())
            return removed

    def revert(self, dealt_cards):
        """
        Takes the top unflipped card and places it back into the unflipped pile. Only used when we dealt out cards
        incorrectly, and we need to undo our changes.
        :param dealt_cards: A CardSequence object.
        :return: This object.
        """
        if self.flipped:
            self.unflipped.append(self.flipped.pop().flip_down())
        self.flipped.extend(dealt_cards.cards)
        return self

    def is_empty(self):
        """
        Determines whether the Tableau is empty. Overrides from CardStack.
        :return: True if it is, False otherwise.
        """
        return len(self.unflipped) == 0 and len(self.flipped) == 0

    def __repr__(self):
        """
        Constructs the string representation of a tableau.
        :return: The string representation.
        """
        string = ""
        for card in self.unflipped + self.flipped:
            string = string + str(card)
        return string



