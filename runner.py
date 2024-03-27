from strategys import *
from board import Board
from config import ROUNDS
from utils import get_pairs


board = Board()

ALL_STRATEGIES = [
    random_move,
    cooperate,
    defect,
    copy_last,
    coop_until_def,
    forgive,
    oponent_average

]


def main():
    """
    Simulate a game between all possible pairs of strategies.
    
    This function iterates over all possible pairs of strategies and 
    simulates a game for a number of rounds defined by ROUNDS.
    After each simulation, the strategies' names are written to the board,
    and then the board is cleared.
    """
    # Get all possible pairs of strategies
    pairs = get_pairs(ALL_STRATEGIES)

    # Iterate over all pairs of strategies
    for pair in pairs:
        # Get the strategies of the pair
        max_strategy = pair[0]
        min_strategy = pair[1]

        # Simulate the game for number of rounds defined by ROUNDS
        for _ in range(ROUNDS):
            # Get the moves of the strategies for the current round
            max_move = max_strategy(board, player=0)
            min_move = min_strategy(board, player=1)
            # Make the moves on the board
            board.make_move(max_move, min_move)

        # Write the names of the strategies to the board
        board.write(max_strategy.__name__, min_strategy.__name__)
        # Clear the board for the next pair of strategies
        board.clear()

if __name__ == "__main__":
    main()
