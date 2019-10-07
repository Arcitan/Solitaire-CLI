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
        self.foundations = {suit: Foundation(suit) for suit in SUITS}
        self.waste = Waste()
        # Deal cards face-down into each of the seven tableaus from the stock.
        # Each tableau has as many cards as its number.
        self.tableaus = [Tableau(self.stock.deal(num, face_up=False)) for num in range(1, 8)]

    def game_won(self):
        """
        Checks if all the foundations are full.
        :return: True if they are, False otherwise.
        """
        return all((foundation.is_full() for foundation in self.foundations.values()))

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
        card = CardSequence(self.stock.deal(face_up=True))
        self.waste.add_card(card)
        return True

    def tableau_to_tableau(self, source_num, dest_num):
        """
        Moves a CardSequence from the top of one tableau and attaches it to the top of another.
        :param source_num: The number of the source Tableau. Must be between 1-7.
        :param dest_num: the number of the destination Tableau. Must be between 1-7.
        :return: True if successful, False otherwise.
        """
        if not dest_num.isdigit() or not source_num.isdigit():
            print("Invalid tableau number specified. Must between 1-7.")
            return False
        dest_num = int(dest_num)
        source_num = int(source_num)
        if not (1 <= source_num <= 7 and 1 <= dest_num <= 7):
            print("Invalid tableau numbers specified. Must be between 1-7.")
            return False
        source = self.tableaus[source_num - 1]
        dest = self.tableaus[dest_num - 1]
        # Take all the flipped cards from the top of the source
        moved_cards = CardSequence(source.deal(len(source)))
        # and attempt to add them to the destination
        if dest.add_card_sequence(moved_cards):
            return True
        else:
            # we were unsuccessful, so put the cards back
            source.revert(moved_cards)
            return False

    def waste_to_tableau(self, dest_num):
        """
        Moves a card (as a CardSequence) from the top of the waste pile to the top of a tableau.
        :param dest_num: The number of the destination Tableau. Must be between 1-7.
        :return: True if successful, False otherwise.
        """
        if not dest_num.isdigit():
            print("Invalid tableau number specified. Must between 1-7.")
            return False
        dest_num = int(dest_num)
        if not 1 <= dest_num <= 7:
            print("Invalid tableau number specified. Must between 1-7.")
            return False
        if self.waste.is_empty():
            print("Waste is empty -- there's nothing to move out of it!")
            return False
        dest = self.tableaus[dest_num - 1]
        card = CardSequence(self.waste.deal(face_up=True))
        if dest.add_card_sequence(card):
            return True
        else:
            # we were unsuccessful, so put the card back
            self.waste.add_card(card)
            return False

    def waste_to_foundation(self, suit):
        """
        Moves a card (as a CardSequence) from the top of the waste to the <suit> foundation.
        :param suit: The Foundation type.
        :return: True if successful, False otherwise.
        """
        if suit not in SUITS:
            print("Invalid suit specified. Must be one of: clubs/diamonds/hearts/spades.")
            return False
        if self.waste.is_empty():
            print("Waste is empty -- there's nothing to move out of it!")
            return False
        card = CardSequence(self.waste.deal(face_up=True))
        dest = self.foundations[suit]
        if dest.add_card(card):
            return True
        else:
            self.waste.add_card(card)
            return False

    def tableau_to_foundation(self, source_num, suit):
        """
        Moves a card from the top of one tableau to a foundation.
        :param source_num: The number of the source Tableau. Must be between 1-7.
        :param suit: The Foundation type.
        :return: True if successful, False otherwise
        """
        if not source_num.isdigit():
            print("Invalid tableau number specified. Must between 1-7.")
            return False
        source_num = int(source_num)
        if not 1 <= source_num <= 7:
            print("Invalid tableau number specified. Must between 1-7.")
            return False
        if suit not in SUITS:
            print("Invalid suit specified. Must be one of: clubs/diamonds/hearts/spades.")
            return False
        source = self.tableaus[source_num - 1]
        dest = self.foundations[suit]
        card = CardSequence(source.deal(face_up=True))
        if dest.add_card(card):
            return True
        else:
            # we were unsuccessful, so put the card back
            source.revert(card)
            return False

    @staticmethod
    def show_possible_moves():
        """
        Prints the list of possible moves.
        :return: A string of possible moves.
        """
        print("Possible moves:")
        print("\t\\sw - Moves a card from Stock to Waste.")
        print("\t\\wf <suit> - Moves a card from Waste to the <suit> Foundation. Suit must be one of: "
              "clubs/diamonds/hearts/spades.")
        print("\t\\wt <tableau_num> - Moves a card from Waste to the <tableau_num> Tableau. <tableau_num> must be "
              "between 1 and 7, inclusive. ")
        print("\t\\tf <tableau_num> <suit> - Moves a card from the <tableau_num> Tableau to the <suit> foundation. "
              "Same input rules as above. ")
        print("\t\\tt <num_1> <num_2> - Moves all face-up cards from <num_1> Tableau to <num_2> Tableau. Same input "
              "rules as above. ")
        print("\t\\help - Displays all possible moves. ")
        print("\t\\quit - Quit the game.\n")

    def display_board(self):
        """
        Displays the game board in a user-friendly visual format.
        :return: A string representing the game board.
        """
        print(f"{BREAK_STRING}\n")
        print(f"STOCK \t WASTE \t\t\t\tFOUNDATION\n")
        print(f"{self.stock}\t{self.waste}\t\t\t\t{self.foundations['clubs']}\t{self.foundations['diamonds']}"
              f"\t{self.foundations['hearts']}\t{self.foundations['spades']}\n")
        print(f"\nTABLEAU\n")
        for num in range(1, 8):
            print(f"{num} {self.tableaus[num-1]}")
        print(f"{BREAK_STRING}\n")
