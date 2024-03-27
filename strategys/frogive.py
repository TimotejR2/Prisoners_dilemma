from config import COOPERATE, DEFECT
def forgive(board, player):
    # Same as copy_last but after 3 defects will it cooperate
    if not board.get_moves():
        return COOPERATE

    # Cooperate if enemy last round cooperated
    last_round = board.get_moves()[-1]
    oposite_player = 1 if player == 0 else 0
    oposite_player_last_round = last_round[oposite_player]
    if oposite_player_last_round == COOPERATE:
        return COOPERATE

    # Cooperate if enemy defected 3 times in a row
    all_moves = board.get_moves()
    for move in all_moves[-4:-2]:
        if move[0] == COOPERATE or move[1] == COOPERATE:
            return DEFECT

    return COOPERATE