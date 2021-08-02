from game_parser import (parse, read_lines)
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

# Integration test (parse and read_lines)

def test_cases():
    # Pos test case
    pos_case_in = "test_game_parser.txt"
    pos_case_out = [
        [Wall(), Wall(), Wall(), Start(0,3), Wall()],
        [Wall(), Water(1,1), Air(1,2), Air(1,3), Wall()],
        [Wall(), Fire(2,1), Teleport('1',2,2), Wall(), Wall()],
        [Wall(), Wall(), Wall(), Teleport('1','3','3'), Wall()],
        [Wall(), Wall(), Wall(), End(4,3), Wall()]
    ]
    
    testing = read_lines(pos_case_in)

    i = 0
    while i < len(testing):
        j = 0
        while j < len(testing[i]):
            assert type(testing[i][j]) == type(pos_case_out[i][j]), (testing[i][j], pos_case_out[i][j])
            j += 1
        i += 1
    
    # Neg case, file not found
    flag_raised = False
    try:
        read_lines("what.txt")
    except FileNotFoundError as e:
        if str(e) == "what.txt does not exist!":
            flag_raised = True
    if not flag_raised:
        assert False

def run_tests():
    test_cases()

run_tests()
