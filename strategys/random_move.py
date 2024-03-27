import random
from config import COOPERATE, DEFECT
def random_move(board, player):
    return random.choice([COOPERATE, DEFECT])