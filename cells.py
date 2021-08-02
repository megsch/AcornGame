class Start:
    def __init__(self, row, col):
        self.display = 'X'
        self.row = row
        self.col = col

    def step(self, game, user_move):
        game.player.record_move(self.row, self.col, user_move)
        message = None
        end_game_well = None
        return message, end_game_well


class End:
    def __init__(self, row, col):
        self.display = 'Y'
        self.row = row
        self.col = col

    def step(self, game, user_move):
        game.player.record_move(self.row, self.col, user_move)
        message = 'You conquer the treacherous maze set up by the Fire Nation and reclaim the' \
        ' Honourable Furious Forest Throne, restoring your hometown back to its former' \
        ' glory of rainbow and sunshine! Peace reigns over the lands.'
        end_game_well = True
        return message, end_game_well


class Air:
    def __init__(self, row, col):
        self.display = ' '
        self.row = row
        self.col = col

    def step(self, game, user_move):
        game.player.record_move(self.row, self.col, user_move)
        message = None
        end_game_well = None
        return message, end_game_well


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game, user_move):
        message = 'You walked into a wall. Oof!'
        end_game_well = None
        return message, end_game_well


class Fire:
    def __init__(self, row, col):
        self.display = 'F'
        self.row = row
        self.col = col

    def step(self, game, user_move):
        game.player.record_move(self.row, self.col, user_move)
        if game.player.num_water_buckets > 0:
            message = 'With your strong acorn arms, you throw a water bucket at the fire.' \
            ' You acorn roll your way through the extinguished flames!'
            game.player.num_water_buckets -= 1
            game.grid[self.row][self.col] = Air(self.row, self.col)
            end_game_well = None
            return message, end_game_well
        else:
            message = 'You step into the fires and watch your dreams disappear :(.'
            end_game_well = False
            return message, end_game_well


class Water:
    def __init__(self, row, col):
        self.display = 'W'
        self.row = row
        self.col = col

    def step(self, game, user_move):
        game.player.record_move(self.row, self.col, user_move)
        game.player.num_water_buckets += 1
        message = "Thank the Honourable Furious Forest, you've found a bucket of water!"
        game.grid[self.row][self.col] = Air(self.row, self.col)
        end_game_well = None
        return message, end_game_well


class Teleport:
    def __init__(self, display, row, column):
        self.display = display
        self.row = row
        self.col = column
        self.pair = None

    def set_pair(self, list_cells):
        # Set the teleport pair attribute to it's teleport pair
        for row_index, row in enumerate(list_cells):
            for block_index, block in enumerate(row):
                if self.display == block.display and (self.row != row_index or \
                self.col != block_index):
                    self.pair = block
                    block.pair = self

    def step(self, game, user_move):
        if self.pair == None:
            self.set_pair(game.grid)
        
        game.player.record_move(self.pair.row, self.pair.col, user_move)
        
        end_game_well = None
        message = 'Whoosh! The magical gates break Physics as we know it and opens a wormhole' \
        ' through space and time.'
        return message, end_game_well
