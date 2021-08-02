from game import Game
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 run.py <filename> [play]")
    sys.exit()

filename = sys.argv[1]

try:
    game_object = Game(filename)
except FileNotFoundError as e:
    print(e)
    sys.exit()
except ValueError as e:
    print(e)
    sys.exit()
except TypeError as e:
    print(e)
    sys.exit()

game_object.print_grid_string()
print()

while True:

    try:
        user_move = input("Input a move: ").lower().strip()
    except EOFError:
        sys.exit()


    if user_move in ['w','a','s','d','e']:
        # Update player location and move history based on the cell the player
        # will be moving into
        # Message = any message from the cell
        # end_game_well: None = game doesn't end. False = Lose game. True = Win game.
        message, end_game_well = game_object.game_move(user_move)
        
        game_object.print_grid_string()
        print()

        if not message == None and end_game_well == None:
            print(message, end = "\n\n")
        
        if end_game_well:
            print()
            print(message, end = '\n\n')
            game_object.print_moves()
            print()
            print("""=====================
====== YOU WIN! =====
=====================""")
            sys.exit()

        elif end_game_well == False:
            print()
            print(message, end = '\n\n')

            bad_mes = 'The Fire Nation triumphs! The Honourable Furious Forest is' \
            ' reduced to a pile of ash and is scattered to the winds by the next' \
            ' storm... You have been roasted.'

            print(bad_mes, end = '\n\n')
            game_object.print_moves()
            print()
            print("""=====================
===== GAME OVER =====
=====================""")
            sys.exit()

    elif user_move == 'q':
        print()
        print("Bye!")
        sys.exit()

    else:
        game_object.print_grid_string()
        print()
        print("Please enter a valid move (w, a, s, d, e, q).", end = "\n\n")
