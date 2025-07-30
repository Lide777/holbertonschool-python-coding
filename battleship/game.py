from config import BOARD_SIZE, SHIP_SPECS
from board import create_board, print_board
from ships import create_fleet, deploy_fleet
from shots import get_valid_shot, get_cpu_shot, process_shot


def main():
    player_board = create_board()
    cpu_board = create_board()

    player_fleet = create_fleet(SHIP_SPECS)
    cpu_fleet = create_fleet(SHIP_SPECS)

    player_map = deploy_fleet(player_board, player_fleet)
    cpu_map = deploy_fleet(cpu_board, cpu_fleet)

    player_shots = set()
    cpu_shots = set((r, c) for r in range(BOARD_SIZE)
                    for c in range(BOARD_SIZE))

    while True:
        print("\nYour Board:")
        print_board(player_board)

        print("\nCPU's Board:")
        print_board(cpu_board, hide_ships=True)

        # Player turn
        row, col = get_valid_shot(player_shots)
        player_shots.add((row, col))
        process_shot(cpu_board, cpu_map, row, col)

        if all(ship.is_sunk() for ship in cpu_fleet):
            print("🎉 You win!")
            break

        # CPU turn
        row, col = get_cpu_shot(cpu_shots)
        print(f"\nCPU fires at {chr(ord('A') + row)}{col + 1}")
        process_shot(player_board, player_map, row, col)

        if all(ship.is_sunk() for ship in player_fleet):
            print("💀 CPU wins!")
            break


if __name__ == "__main__":
    main()
