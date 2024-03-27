from config import COOPERATE
def copy_last(board, player):
    if not board.get_moves():
        return COOPERATE

    last_round = board.get_moves()[-1]
    oposite_player = 1 if player == 0 else 0
    oposite_player_last_round = last_round[oposite_player]
    return oposite_player_last_round