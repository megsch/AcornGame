import sys
from game import Game

if len(sys.argv) != 3:
    print("Usage: python3 solver.py <filename> <mode>")
    sys.exit()

filename = sys.argv[1]
mode = sys.argv[2]

try:
    game_object = Game(filename)
except FileNotFoundError as e:
    print(e)
    sys.exit()

game_object.player.set_start_pos(game_object.grid)

def add_walk(node, move, queue):
    # Move player
    message, end_game_well = node.game.game_move(move)
    if message == "Thank the Honourable Furious Forest, you've found a bucket of water!":
        node.visited_cells = []

    # If the player has won
    if end_game_well:
        winner = node
        return winner

    # Has player hit a wall or died?
    if message != "You walked into a wall. Oof!" and end_game_well != False:   

        # Add to visited cells
        node.add_to_visited_cells()
        add_to_queue = node.can_revisit()
        
        if add_to_queue:
            queue.append(node)
        
    winner = None
    return winner

def copy_list_1D(lst):
    copied_list = []
    for l in lst:
        copied_list.append(l)
    return copied_list

def copy_list_2D(lst):
    copied_list = []
    # For 2D lists
    for lists in lst:
        copied_list.append(lists[:])

    return copied_list

class Node:
    def __init__(self, game):
        self.game = game
        self.visited_cells = []

    def copy_node(node, parent_node):
        node.game.player.row = parent_node.game.player.row
        node.game.player.col = parent_node.game.player.col 
        node.game.grid = copy_list_2D(parent_node.game.grid)
        node.game.player.move_history = copy_list_1D(parent_node.game.player.move_history)
        node.game.player.num_water_buckets = parent_node.game.player.num_water_buckets
        node.visited_cells = parent_node.visited_cells[:]

    def add_to_visited_cells(self):
        # Adds the player's cell location to the visited cell list
        visited_at_least_once = False
        for cells in self.visited_cells:
            if (self.game.player.row, self.game.player.col) == cells[0]:
                visited_at_least_once = True
                cells[1] += 1
                break
        if visited_at_least_once == False:
            cell = [(self.game.player.row, self.game.player.col), 1]
            self.visited_cells.append(cell)

    def can_revisit(self):
        # Return True, add game to queue
        for cells in self.visited_cells:
            if (self.game.player.row, self.game.player.col) == cells[0]:
                if cells[1] < 2:
                    return True
                else:
                    return False

        return True   
                
        

def solve(mode, filename):
    # Instantiate a new node every move
    node_object = Node(Game(filename))
    node_object.add_to_visited_cells()

    queue = [node_object]
    winner = None
    move_list = ['s', 'a', 'd', 'w', 'e']

    while queue: 

        if mode == 'BFS':
            first_node_queued = queue.pop(0)
        elif mode == 'DFS':
            first_node_queued = queue.pop()
        
        for move in move_list:

            # Copy Node instance
            node_next_move = Node(Game(filename))
            Node.copy_node(node_next_move, first_node_queued)
            

            # Make move and add to queue
            winner = add_walk(node_next_move, move, queue)

            # Is there a winner?
            if winner != None:
                # Return a message of path
                string = ""
                for move in winner.game.player.move_history:
                    string += move
                    string += ", "
                string = string.strip(", ")

                if len(winner.game.player.move_history) == 1:
                    message = """Path has {} move.
Path: {}""".format(len(winner.game.player.move_history), string)
                else:
                    message = """Path has {} moves.
Path: {}""".format(len(winner.game.player.move_history), string)

                return message
                
        if len(queue) == 0:
            # All possible paths have been found
            break
    
    if winner == None:
        # Return empty message
        message = None
        return message

    else:
        raise ValueError("Usage: python3 solver.py <filename> <mode>")


if __name__ == "__main__":
    message = solve(mode, filename)
    if message != None:
        print(message)
        # Print your solution...
    else:
        print("There is no possible path.")


