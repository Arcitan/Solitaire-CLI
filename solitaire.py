# import dependencies
from src.Game import Game


def main():
    game = Game()
    print("""
  ______             __  __    __                __                     
 /      \           /  |/  |  /  |              /  |                    
/$$$$$$  |  ______  $$ |$$/  _$$ |_     ______  $$/   ______    ______  
$$ \__$$/  /      \ $$ |/  |/ $$   |   /      \ /  | /      \  /      \ 
$$      \ /$$$$$$  |$$ |$$ |$$$$$$/    $$$$$$  |$$ |/$$$$$$  |/$$$$$$  |
 $$$$$$  |$$ |  $$ |$$ |$$ |  $$ | __  /    $$ |$$ |$$ |  $$/ $$    $$ |
/  \__$$ |$$ \__$$ |$$ |$$ |  $$ |/  |/$$$$$$$ |$$ |$$ |      $$$$$$$$/ 
$$    $$/ $$    $$/ $$ |$$ |  $$  $$/ $$    $$ |$$ |$$ |      $$       |
 $$$$$$/   $$$$$$/  $$/ $$/    $$$$/   $$$$$$$/ $$/ $$/        $$$$$$$/ 
                                                                        
                                                                        
                                                                        """)
    game.show_possible_moves()

    while not game.game_won():
        game.display_board()
        command = input("Please enter a move: ")
        command_parts = command.lower().lstrip().rstrip().split()

        if command_parts[0] == "\\quit":
            print("Thank you for playing. Goodbye!")
            break
        elif command_parts[0] == "\\help":
            game.show_possible_moves()
        elif command_parts[0] == "\\sw":
            game.stock_to_waste()
        elif command_parts[0] == "\\wf":
            game.waste_to_foundation(command_parts[1])
        elif command_parts[0] == "\\wt":
            game.waste_to_tableau(command_parts[1])
        elif command_parts[0] == "\\tf":
            game.tableau_to_foundation(command_parts[1], command_parts[2])
        elif command_parts[0] == "\\tt":
            game.tableau_to_tableau(command_parts[1], command_parts[2])
        else:
            print("Invalid move entered. Please enter a valid move. Type '\\help' to see a list of valid moves.")


if __name__ == "__main__":
    main()
