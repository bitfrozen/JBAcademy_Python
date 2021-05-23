def print_table(table_to_print):
    print('-' * 9)
    for i in range(0, 3):
        print('| ' + table_to_print[i][0] + ' ' + table_to_print[i][1] + ' ' + table_to_print[i][2] + ' |')
    print('-' * 9)


def parse_table(input_string):
    parsed_table = [list(input_string[0:3]),
                    list(input_string[3:6]),
                    list(input_string[6:9])]
    return parsed_table


def init_table():
    return [list('___'),
            list('___'),
            list('___')]


def get_user_move(c):
    global table
    while True:
        user_coordinates = input("Enter the coordinates: ").split()  #
        if not all(elem.isdigit() for elem in user_coordinates):
            print("You should enter numbers!")
            continue
        if not all(0 < int(elem) < 4 for elem in user_coordinates):
            print("Coordinates should be from 1 to 3!")
            continue
        if len(user_coordinates) < 2:
            print("Enter two coordinates!")
            continue
        if table[int(user_coordinates[0]) - 1][int(user_coordinates[1]) - 1] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        c += 1
        table[int(user_coordinates[0]) - 1][int(user_coordinates[1]) - 1] = 'O' if c % 2 == 0 else 'X'
        return c


# Get set scans
def judge_move():
    x_win = False
    o_win = False
    # form lookup list
    scan_locations = [[table[0][0], table[0][1], table[0][2]],
                      [table[1][0], table[1][1], table[1][2]],
                      [table[2][0], table[2][1], table[2][2]],
                      [table[0][0], table[1][0], table[2][0]],
                      [table[0][1], table[1][1], table[2][1]],
                      [table[0][2], table[1][2], table[2][2]],
                      [table[0][0], table[1][1], table[2][2]],
                      [table[2][0], table[1][1], table[0][2]]]
    # check for winning combination
    for loc in scan_locations:
        if all([elem == 'X' for elem in loc]):
            x_win = True
            break
    for loc in scan_locations:
        if all([elem == 'O' for elem in loc]):
            o_win = True
            break
    # check symbol count
    flatten = [elem for loc in table for elem in loc]
    too_much = abs(flatten.count('X') - flatten.count('O')) > 1

    # Evaluate board
    if (x_win and o_win) or too_much:
        print("Impossible")
        return False
    elif x_win:
        print("X wins")
        return False
    elif o_win:
        print("O wins")
        return False
    elif flatten.count('_') == 0:
        print("Draw")
        return False
    else:
        return True


table = init_table()
play_game = True
print_table(table)
move_count = 0

while play_game:
    move_count = get_user_move(move_count)
    print_table(table)
    play_game = judge_move()
    if move_count > 8:
        play_game = False

exit(0)
