from cells import Start

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.move_history = []
        self.row = None
        self.col = None

    def set_start_pos(self, cell_list):
        # Set the player position to the Start cell location
        for row_index, row in enumerate(cell_list):
            for block_index, block in enumerate(row):
                if isinstance(block, Start):
                    self.row = row_index
                    self.col = block_index
                    break


    def record_move(self, new_row, new_col, user_move):
        # Move player and record in move history
        # Recieve move that has been checked
        self.row = new_row
        self.col = new_col
        self.move_history.append(user_move)

    def get_move_history(self):
        moves = ""
        for m in self.move_history:
            moves += m
            moves += ", "
        moves = moves.strip(", ")
        return moves

