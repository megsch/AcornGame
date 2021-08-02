from game_parser import parse
from cells import (Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def positive_test_parse():
    
    # Positive case 1, include all cell types
    pos_1_in = [
        "*X**\n",
        "* 1*\n",
        '*F*W\n',
        '*1**\n',
        '*Y**\n'
    ]
    pos_1_out = [
        [Wall(), Start(0,1), Wall(), Wall()],
        [Wall(), Air(1,1), Teleport(1,1,2),Wall()],
        [Wall(), Fire(2,1), Wall(), Water(2,3)],
        [Wall(), Teleport(1,3,1), Wall(), Wall()],
        [Wall(), End(4,1), Wall(), Wall()]
        ]
    
    pos_1_parsed = parse(pos_1_in)
    i = 0
    while i < len(pos_1_parsed):
        j = 0
        while j < len(pos_1_parsed[i]):
            assert type(pos_1_parsed[i][j]) == type(pos_1_out[i][j])
            j += 1
        i += 1

    # Positive case 2, more teleports
    pos_2_in = [
        '*X**\n',
        '*11*\n',
        '*44*\n',
        '***Y\n'
    ]
    pos_2_parsed = parse(pos_2_in)
    pos_2_out = [
        [Wall(),Start(0,1),Wall(),Wall()],
        [Wall(),Teleport(1,1,1),Teleport(1,1,2),Wall()],
        [Wall(),Teleport(4,2,1),Teleport(4,2,2),Wall()],
        [Wall(),Wall(),Wall(),End(3,3)]
    ]

    i = 0
    while i < len(pos_2_parsed):
        j = 0
        while j < len(pos_2_parsed[i]):
            assert type(pos_2_parsed[i][j]) is type(pos_2_out[i][j])
            j += 1
        i += 1

def edge_cases():
    # Some lines have \n
    edge_in = [
        '*X**\n',
        '*  *',
        '**Y*'
    ]
    edge_out = [
        [Wall(),Start(0,1),Wall(),Wall()],
        [Wall(),Air(1,1),Air(1,2),Wall()],
        [Wall(),Wall(),End(2,2),Wall()]
    ]
    edge_parsed = parse(edge_in)
    for row_index, row in enumerate(edge_parsed):
        for block_index, block in enumerate(row):
            assert type(block) is type(edge_out[row_index][block_index])


def negative_cases():
    # Neg case, not list
    neg_1_in = 8
    flag_raised = False
    try:
        parse(neg_1_in)
    except TypeError as e:
        if str(e) == 'Enter a list of strings.':
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, No start
    neg_2_in = [
        '****\n',
        '** *\n',
        '**Y*\n'
    ]
    flag_raised = False
    try:
        parse(neg_2_in)
    except ValueError as e:
        if str(e) == "Expected 1 starting position, got 0.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, No end
    neg_3_in = [
        '**X*\n',
        '*W**\n',
        '****\n'
    ]

    flag_raised = False
    try:
        parse(neg_3_in)
    except ValueError as e:
        if str(e) == "Expected 1 ending position, got 0.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, 3 starts
    neg_4_in = [
        '*X**\n',
        '*XX*\n',
        '*Y**\n'
    ]
    flag_raised = False
    try:
        parse(neg_4_in)
    except ValueError as e:
        if str(e) == "Expected 1 starting position, got 3.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, 5 ends
    neg_5_in = [
        '*X**\n',
        '*YY*\n',
        '*Y*Y\n',
        '*Y**\n'
    ]
    flag_raised = False
    try:
        parse(neg_5_in)
    except ValueError as e:
        if str(e) == "Expected 1 ending position, got 5.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, 1 teleport
    neg_6_in = [
        '*X**\n',
        '*1**\n',
        '***Y\n'
    ]
    flag_raised = False
    try:
        parse(neg_6_in)
    except ValueError as e:
        if str(e) == "Teleport pad 1 does not have an exclusively matching pad.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, +2 teleport
    neg_7_in = [
        '*X**\n',
        '*1*1\n',
        '*1**\n',
        '*Y**\n'
    ]
    flag_raised = False
    try:
        parse(neg_7_in)
    except ValueError as e:
        if str(e) == "Teleport pad 1 does not have an exclusively matching pad.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Neg case, random characters
    neg_8_in = [
        '**X*\n',
        '*(*F\n',
        '**&Y\n'
    ]
    flag_raised = False
    try:
        parse(neg_8_in)
    except ValueError as e:
        if str(e) == "Bad letter in configuration file: (.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Uneven no. of teleports, no start or end, random letter
    # Should raise bad letter first
    neg_9_in = [
        "***",
        "*8*",
        "d**"
    ]
    flag_raised = False
    try:
        parse(neg_9_in)
    except ValueError as e:
        if str(e) == "Bad letter in configuration file: d.":
            flag_raised = True
    if not flag_raised:
        assert False

    # Test teleport '0', return ValueError
    neg_10_in = [
        "*X**",
        "*0**",
        "*Y**"
    ]
    flag_raised = False
    try:
        parse(neg_10_in)
    except ValueError as e:
        if str(e) == "Bad letter in configuration file: 0.":
            flag_raised = True
    if not flag_raised:
        assert False



def run_tests():
    positive_test_parse()
    edge_cases()
    negative_cases()

run_tests()
