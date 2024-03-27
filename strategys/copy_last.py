import random
from config import COOPERATE, DEFECT

def copy_last(board, player):
    if not board.get_moves():
        return COOPERATE

    last_round = board.get_moves()[-1]
    oposite_player = 1 if player == 0 else 0
    oposite_player_last_round = last_round[oposite_player]
    return oposite_player_last_round

def copy_last_agressive(board, player):
    move = copy_last(board, player)
    if move == COOPERATE:
        return random.choices([COOPERATE, DEFECT], weights=[0.8, 0.2], k=1)[0]
    return move

def copy_last_very_agressive(board, player):
    move = copy_last(board, player)
    if move == COOPERATE:
        return random.choices([COOPERATE, DEFECT], weights=[0.5, 0.5], k=1)[0]
    return move

def copy_last_nice(board, player):
    move = copy_last(board, player)
    if move == DEFECT:
        return random.choices([COOPERATE, DEFECT], weights=[0.2, 0.8], k=1)[0]
    return move

def coop_until_def(board, player):
    """
    Cooperate until defect, then only defect
    """
    if not board.get_moves():
        return COOPERATE

    last_round = board.get_moves()[-1]
    if last_round[0] == DEFECT or last_round[1] == DEFECT:
        return DEFECT

    return COOPERATE