"""
Main code that simulates all possible pairs of strategies.
"""
import multiprocessing
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
    copy_last_agressive,
    copy_last_nice,
    coop_until_def,
    forgive,
    oponent_average,
    copy_last_very_agressive,
    coop_if_3_in_a_row,
    def_if_3_in_a_row

]



def simulate_game(pair):
    """
    Simulate a game between a pair of strategies.
    """
    max_strategy, min_strategy = pair
    for _ in range(ROUNDS):
        max_move = max_strategy(board, player=0)
        min_move = min_strategy(board, player=1)
        board.make_move(max_move, min_move)
    board.write(max_strategy.__name__, min_strategy.__name__)
    board.clear()

def main():
    # Get all possible pairs of strategies
    pairs = get_pairs(ALL_STRATEGIES)

    # Create a multiprocessing pool
    pool = multiprocessing.Pool()

    # Map the simulate_game function to each pair of strategies
    pool.map(simulate_game, pairs)

    # Close the pool to free up resources
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
