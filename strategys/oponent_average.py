from config import COOPERATE, DEFECT

def oponent_average(board, player):
    return oponent_average_last_n(board, player, 0)

def oponent_average_last_n(board, player, n):
    all_moves = board.get_moves()
    if not all_moves:
        return COOPERATE
    
    oponent = 1 if player == 0 else 0
    coop = 0
    defects = 0

    # If no limit
    if n == 0:
        for games in all_moves:
            if games[oponent] == COOPERATE:
                coop += 1
            else:
                defects += 1
    else:
        for games in all_moves[-n:]:
            if games[oponent] == COOPERATE:
                coop += 1
            else:
                defects += 1

    if defects > coop:
        return DEFECT
    else:
        return COOPERATE
    
    
    