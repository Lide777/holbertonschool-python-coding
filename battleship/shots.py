from config import BOARD_SIZE
import random


def get_valid_shot(tried_shots):
    while True:
        shot = input("Enter target (e.g. B3): ").strip().upper()
        if len(shot) < 2:
            print("Invalid input.")
            continue

        row_char, col_str = shot[0], shot[1:]
        if not col_str.isdigit():
            print("Invalid column.")
            continue

        row = ord(row_char) - ord('A')
        col = int(col_str) - 1

        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if (row, col) not in tried_shots:
                return (row, col)
            else:
                print("Already tried.")
        else:
            print("Out of bounds.")


def get_cpu_shot(available_shots):
    shot = random.choice(list(available_shots))
    available_shots.remove(shot)
    return shot


def process_shot(board, coord_map, row, col):
    if (row, col) in coord_map:
        board[row][col] = 'X'
        ship = coord_map[(row, col)]
        ship.register_hit()
        print("Hit!")
        if ship.is_sunk():
            print("Ship sunk!")
    else:
        board[row][col] = 'O'
        print("Miss.")
