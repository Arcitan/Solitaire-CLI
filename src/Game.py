# import dependencies
from src.Stock import Stock, SUITS
from src.Foundation import Foundation
from src.Waste import Waste
from src.Tableau import Tableau

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
        if len(self.stock) == 0 and len(self.waste) == 0:
            print("There are no cards left to move!")
            return False
        elif len(self.stock) == 0:
            self.waste.cards.reverse()
            self.stock.refill(self.waste.deal(len(self.waste), face_up=False))


