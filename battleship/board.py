from config import BOARD_SIZE

def create_board():
    return [['~' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_headers():
    header = "  " + " ".join(str(i + 1) for i in range(BOARD_SIZE))
    print(header)

def print_board(board, hide_ships=False):
    print_headers()
    for i, row in enumerate(board):
        row_label = chr(ord('A') + i)
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append('~')
            else:
                display_row.append(cell)
        print(f"{row_label} " + " ".join(display_row))