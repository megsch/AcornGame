from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import sys


def read_lines(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("{} does not exist!".format(filename))

    lines = f.readlines()
    list_of_cells = parse(lines)
    return list_of_cells



def parse(lines):
    if not isinstance(lines, list):
        raise TypeError("Enter a list of strings.")
    for string in lines:
        if not isinstance(string,str):
            raise TypeError("Enter a list of strings.")

    no_of_starts = 0
    no_of_ends = 0
    teleport_signs = ["1",'2','3','4','5','6','7','8','9']
    teleports_used = []

    list_cells = []

    for row_index, row in enumerate(lines):
        current_row = []
        appended_new_row = False
        for block_index, block in enumerate(row):
            if block == "X":
                current_row.append(Start(row_index, block_index))
                no_of_starts += 1

            elif block == 'Y':
                current_row.append(End(row_index, block_index))
                no_of_ends += 1
            
            elif block == " ":
                current_row.append(Air(row_index, block_index))
            
            elif block == "*":
                current_row.append(Wall())

            elif block == "F":
                current_row.append(Fire(row_index, block_index))

            elif block == "W":
                current_row.append(Water(row_index, block_index))

            elif block in teleport_signs:
                tel_block = Teleport(block, row_index, block_index)
                current_row.append(tel_block)
                
                teleport_already_initiated = False
                for tel in teleports_used:
                    if tel_block.display == tel[0]:
                        tel[1] += 1
                        teleport_already_initiated = True     
                
                if not teleport_already_initiated:
                    teleports_used.append([tel_block.display,1])

            elif block == '\n':
                pass

            else:
                raise ValueError("Bad letter in configuration file: {}.".format(block))

        list_cells.append(current_row)


    if no_of_starts != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(no_of_starts))


    if no_of_ends != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(no_of_ends))


    for tel in teleports_used:
        if tel[-1] != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(tel[0]))

    return list_cells
