from config import COOPERATE, DEFECT

def def_if_3_in_a_row(board, player):
    """
    Defect if 3 defects in a row, otherwise cooperate
    """

    if len(board.get_moves()) >=3:
        # If 3 defects in row, defect
        if all(move[0] == DEFECT for move in board.get_moves()[-3:]):
            return DEFECT
    return COOPERATE
