from game import Game


def test_game():
    # Make game object and test game attributes
    filename = 'board_water.txt'
    try:
        game_test = Game(filename)
    except FileNotFoundError as e:
        assert False, e
    assert game_test.grid_no_cols == 5
    assert game_test.grid_no_rows == 3
    assert game_test.player.row == 0
    assert game_test.player.col == 2

    # Check game_move()
    # Check move 'w' outside of cell
    message, end_game_well = game_test.game_move('w')
    assert message == "You walked into a wall. Oof!"
    assert end_game_well == None
    assert game_test.player.col == 2
    assert game_test.player.row == 0
    # Check move 'a' into wall
    message, end_game_well = game_test.game_move('a')
    assert message == "You walked into a wall. Oof!"
    assert end_game_well == None
    assert game_test.player.col == 2
    assert game_test.player.row == 0
    # Reset player location, check move 'd' into water
    game_test.player.row = 1
    game_test.player.col = 2
    message, end_game_well = game_test.game_move('d')
    assert message == "Thank the Honourable Furious Forest, you've found a bucket of water!"
    assert end_game_well == None
    assert game_test.player.row == 1
    assert game_test.player.col == 3
    # Reset player location, check move 'a' into fire
    game_test.player.row = 1
    game_test.player.col = 2
    message, end_game_well = game_test.game_move('a')
    assert message == 'With your strong acorn arms, you throw a water bucket at the fire.' \
            ' You acorn roll your way through the extinguished flames!'
    assert end_game_well == None
    assert game_test.player.row == 1
    assert game_test.player.col == 1
    # Check move 's' into End
    message, end_game_well = game_test.game_move('s')
    assert message == 'You conquer the treacherous maze set up by the Fire Nation and reclaim the' \
        ' Honourable Furious Forest Throne, restoring your hometown back to its former' \
        ' glory of rainbow and sunshine! Peace reigns over the lands.'
    assert end_game_well == True
    assert game_test.player.row == 2
    assert game_test.player.col == 1


def run_tests():
    test_game()

test_game()
