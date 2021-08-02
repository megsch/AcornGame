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


def test_grid():
    # Test 1, A in X cell
    player = Player()
    player.row = 0
    player.col = 1

    grid = [
        [Wall(),Start(0,1),Wall(),Wall()],
        [Wall(),Teleport('1',1,1),Teleport('1',1,2),Wall()],
        [Wall(),Teleport('4',2,1),Teleport('4',2,2),Wall()],
        [Wall(),Wall(),Wall(),End(3,3)]
    ]
    string_output = "*A**\n" \
        '*11*\n'\
        '*44*\n'\
        '***Y\n'\
        '\n'\
        'You have 0 water buckets.'

    assert grid_to_string(grid, player) == string_output

    # Test 2, Acorn in an Air cell and water bucket
    player.row = 1
    player.col = 1
    player.num_water_buckets += 1
    grid = [
        [Wall(), Start(0,1), Wall(), Wall()],
        [Wall(), Air(1,1), Teleport('1',1,2),Wall()],
        [Wall(), Teleport('1',3,1), Wall(), Wall()],
        [Wall(), End(3,1), Wall(), Wall()]
    ]
    string_output = "*X**\n"\
        '*A1*\n'\
        '*1**\n'\
        '*Y**\n'\
        '\n'\
        'You have 1 water bucket.'
    
    assert grid_to_string(grid, player) == string_output

    # Test 3, Acorn in water
    grid = [
        [Wall(), Start(0,1), Wall()],
        [Wall(), Water(1,1), End(1,2)]
    ]
    player.row = 1
    player.col = 1
    player.num_water_buckets = 2
    string_output = "*X*\n"\
        '*AY\n'\
        '\n'\
        'You have 2 water buckets.'
    assert grid_to_string(grid, player) == string_output

def run_tests():
    test_grid()

run_tests()

# Only positive tests are needed since the information that is passed 
# to grid_to_string() is controlled
