from config import COOPERATE, DEFECT

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