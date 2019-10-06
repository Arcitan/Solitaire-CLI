SUITS_SYMBOLS = {"white": {"spades": u"\u2664",
                           "hearts": u"\u2661",
                           "diamonds": u"\u2662",
                           "clubs": u"\u2667"},
                 "black": {"spades": u"\u2660",
                           "hearts": u"\u2665",
                           "diamonds": u"\u2666",
                           "clubs": u"\u2663"}}


class Card:
    """
    A class that represents a typical playing card.
    """
    def __init__(self, color, rank, suit, face_down=False):
        """
        Constructor for a card.
        :param suit: A string -- spades, hearts, diamonds, or clubs.
        :param rank: A string -- 2-10, A, J, K, or Q.
        :param color: A string -- white or black.
        :param face_down: A boolean indicating whether the card is face-down or not.
        """
        self.suit = suit
        self.rank = rank
        self.color = color
        self.value = self.get_value(rank)
        self.face_down = face_down

    @staticmethod
    def get_value(rank):
        """
        Get the numeric value (1-13) associated with a card's rank.
        :param rank: A string of either 2-10, A, J, K, or Q.
        :return: An integer between 1-13.
        """
        face_vals = {"J": 11, "Q": 12, "K": 13, "A": 1}
        return int(rank) if rank.isdigit() else face_vals[rank]

    def is_under(self, card):
        """
        Determines whether this card is "under" the value of another card.
        :param card: Another Card object.
        :return: True if it is, False otherwise.
        """
        return card.value == self.value + 1

    def is_opposite_color(self, card):
        """
        Determines whether this card is the opposite color of another card.
        :param card: Another Card object.
        :return: True if it is, False otherwise.
        """
        return card.color != self.color

    def can_attach_to(self, card):
        """
        Determines whether we can attach this card to another card.
        :param card: Another Card object.
        :return: True if we can, False otherwise.
        """
        return self.is_opposite_color(card) and self.is_under(card)

    def __repr__(self):
        """
        Constructs the string representation of a card. Will be the rank followed by the suit symbol in unicode.
        :return: The string representation of a card.
        """
        if self.face_down:
            return "--"
        return f"[{self.rank}{SUITS_SYMBOLS[self.color][self.suit]}]"

    def flip_up(self):
        """
        Flips the card face-up.
        :return: This card.
        """
        self.face_down = False
        return self

    def flip_down(self):
        """
        Flips the card face-down.
        :return: This card.
        """
        self.face_down = True
        return self

