def grid_to_string(grid, player):
    string = ''
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if player.col == column_index and player.row == row_index:
                string += player.display

            else:
                string += column.display
        string += '\n'
    
    if player.num_water_buckets == 1:
        water_bucket_mes = '\nYou have 1 water bucket.'
    else:
        water_bucket_mes = '\nYou have {} water buckets.'.format(player.num_water_buckets)
    string += water_bucket_mes
    return string
