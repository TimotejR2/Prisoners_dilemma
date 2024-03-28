from config import COOPERATE, DEFECT

def coop_if_3_in_a_row(board, player):
    """
    Cooperate if 3 coops in a row, otherwise defect
    """

    if len(board.get_moves()) >=3:
        # If 3 coops in row, coop
        if all(move[0] == COOPERATE for move in board.get_moves()[-3:]):
            return COOPERATE
        return DEFECT
    
    return COOPERATE
