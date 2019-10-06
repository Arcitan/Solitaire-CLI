# import dependencies
from src.Stock import Stock, SUITS
from src.Foundation import Foundation
from src.Waste import Waste
from src.Tableau import Tableau
from src.CardSequence import CardSequence

BREAK_STRING = "================================================================================="


class Game:
    """
    Class that handles playing the game of Solitaire.
    """
    def __init__(self):
        """
        Constructor for the game object. Handles initial setup.
        """
        self.stock = Stock()
        self.foundations = [Foundation(suit) for suit in SUITS]
        self.waste = Waste()
        # Deal cards face-down into each of the seven tableaus from the stock.
        # Each tableau has as many cards as its number.
        self.tableaus = [Tableau(self.stock.deal(num, face_up=False)) for num in range(1, 8)]

    def game_won(self):
        """
        Checks if all the foundations are full.
        :return: True if they are, False otherwise.
        """
        return all((foundation.is_full() for foundation in self.foundations))

    def stock_to_waste(self):
        """
        Moves a card from the stock to the waste pile.
        :return: True if it was successful, False otherwise.
        """
        # If both the stock and waste are empty, then we can't do anything
        if len(self.stock) == 0 and len(self.waste) == 0:
            print("There are no cards left to move!")
            return False
        # If only the stock is empty, first take everything in the waste and re-add it to the stock (upside-down)
        elif len(self.stock) == 0:
            self.waste.cards.reverse()
            self.stock.refill(self.waste.deal(len(self.waste), face_up=False))
        # Take the top card from the stock and add it face-up to the waste
        self.waste.add_card(self.stock.deal(face_up=True))
        return True

    def tableau_to_tableau(self, source, dest):
        """
        Moves a CardSequence from the top of one tableau and attaches it to the top of another.
        :param source: A Tableau object. Where the CardSequence is being taken from.
        :param tab2: A Tableau object. Where the CardSequence is going to be attached to.
        :return: True if successful, False otherwise.
        """
        # Take all the flipped cards from the top of the source
        moved_cards = CardSequence(source.deal(len(source)))

        # and attempt to add them to the destination
        return dest.add_card_sequence(moved_cards)
