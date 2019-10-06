
class CardStack:
    """
    Base class for a stack of cards.
    Will be inherited by the Tableau, Stock, Waste, and Foundation classes.
    """
    def __init__(self):
        self.cards = []

    def peek_top(self, num=1):
        """
        Returns the top *num* cards, without modifying the stack.
        :param num: The number of cards to peek at. Default is 1.
        :return: If num > 1, returns a list of the top *num* cards. Otherwise, just returns a single Card object.
        """
        if self.is_empty():
            print("Cannot peek into an empty stack.")
        if num > len(self.cards):
            print("Cannot peek more cards than are in the stack.")
        if num > 1:
            return self.cards[-num:]
        return self.cards[-1]

    def peek_bottom(self, num=1):
        """
        Returns the bottom *num* cards, without modifying the stack.
        :param num: The number of cards to peek at. Default is 1.
        :return: If num > 1, returns a list of the bottom *num* cards. Otherwise, just returns a single Card object.
        """
        if self.is_empty():
            print("Cannot peek into an empty stack.")
        if num > len(self.cards):
            print("Cannot peek more cards than are in the stack.")
        if num > 1:
            return self.cards[:num]
        return self.cards[0]

    def deal(self, num=1, face_up=True):
        """
        Returns the top *num* cards, and removes them from the stack.
        :param num: The number of cards to peek at. Default is 1.
        :param face_up: Whether the cards are dealt face-up or face-down. Default is True (i.e. face-up).
        :return: If num > 1, returns a list of the top *num* cards. Otherwise, just returns a single Card object.
        """
        if self.is_empty():
            raise ValueError("Cannot deal out of an empty stack.")
        if num > len(self.cards):
            raise ValueError("Cannot deal more cards than are in the stack.")
        if face_up:
            return list(reversed([self.cards.pop().flip_up() for _ in range(num)]))
        else:
            return list(reversed([self.cards.pop().flip_down() for _ in range(num)]))

    def __len__(self):
        """
        Called by the len() method. Computes the number of elements in the stack.
        :return: The number of cards in the stack.
        """
        return len(self.cards)

    def is_empty(self):
        """
        Determines whether the stack is empty or not.
        :return: True if it's empty, False otherwise.
        """
        return len(self.cards) == 0
