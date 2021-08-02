from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


class Game:
    def __init__(self, filename):
        try:
            self.grid = read_lines(filename)
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        except ValueError as e:
            raise ValueError(e)
        except TypeError as e:
            raise TypeError(e)
        self.grid_no_cols = len(self.grid[0])
        self.grid_no_rows = len(self.grid)
        self.player = Player()
        self.player.set_start_pos(self.grid)
        self.wall_cell = Wall()

    def print_grid_string(self):
        # Print list of cells as a string
        string = grid_to_string(self.grid, self.player)
        print(string)

    def game_move(self, move):
        # Set up temporary player location
        if move == 'w':
            new_row = self.player.row - 1
            new_col = self.player.col
        elif move == 'a':
            new_row = self.player.row
            new_col = self.player.col - 1
        elif move == 's':
            new_row = self.player.row + 1
            new_col = self.player.col
        elif move == 'd':
            new_row = self.player.row
            new_col = self.player.col + 1
        elif move == 'e':
            new_row = self.player.row
            new_col = self.player.col

        # Does the player move outside the grid?
        if new_row < 0 or new_row >= self.grid_no_rows:
            return self.wall_cell.step(self, move)
        if new_col < 0 or new_col >= self.grid_no_cols:
            return self.wall_cell.step(self, move)

        # Get message and end_game_well from the cell the player will step into
        message, end_game_well = self.grid[new_row][new_col].step(self, move)

        return message, end_game_well
            

    def print_moves(self):
        no_moves = len(self.player.move_history)
        moves = self.player.get_move_history()
                
        if no_moves == 1:
            print("You made {} move.".format(no_moves))
            print("Your move: {}".format(moves))

        else:
            print("You made {} moves.".format(no_moves))
            print("Your moves: {}".format(moves))
