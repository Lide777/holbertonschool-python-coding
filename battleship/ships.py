import random
from config import BOARD_SIZE

class Ship:
    def __init__(self, length):
        self.length = length
        self.positions = []
        self.hits = 0

    def register_hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits >= self.length

def create_fleet(specs):
    return [Ship(length) for length in specs]

def place_ship(board, ship):
    while True:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - ship.length)
            coords = [(row, col + i) for i in range(ship.length)]
        else:
            row = random.randint(0, BOARD_SIZE - ship.length)
            col = random.randint(0, BOARD_SIZE - 1)
            coords = [(row + i, col) for i in range(ship.length)]

        if all(board[r][c] == '~' for r, c in coords):
            for r, c in coords:
                board[r][c] = 'S'
            ship.positions = coords
            return

def deploy_fleet(board, fleet):
    coord_map = {}
    for ship in fleet:
        place_ship(board, ship)
        for pos in ship.positions:
            coord_map[pos] = ship
    return coord_map