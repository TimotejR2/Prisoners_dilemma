"""
Main code that simulates all possible pairs of strategies.
"""
from strategys import *
from board import Board
from config import ROUNDS
from utils import get_pairs


board = Board()

"""
    Tit for Two Tats: Táto stratégia je podobná ako “copy_last”, ale odpovedá na zradu až po dvoch po sebe idúcich zradách od protihráča. Toto môže pomôcť pri zmierňovaní náhodných chýb alebo zmiernení škody z jednorazových zrad.

    Grudger: Táto stratégia začína spoluprácou a pokračuje v spolupráci, pokiaľ protihráč nesiahne po zrade. Akonáhle protihráč zradí, Grudger bude zrádzať na zvyšok hry.

    Pavlov: Táto stratégia, známa aj ako “win-stay, lose-shift”, opakuje posledný ťah, ak bol úspešný (tj. ak bol výsledok spolupráca-spolupráca alebo zrada-zrada), ale mení ťah, ak bol neúspešný (tj. ak bol výsledok spolupráca-zrada alebo zrada-spolupráca).

    Random Tit for Tat: Táto stratégia je variáciou na “Tit for Tat”, kde občas náhodne zmení svoj ťah. Toto môže byť užitočné pre zmiernenie zacyklenia v zrážkach.

    Adaptive: Táto stratégia sa učí a prispôsobuje sa stratégii protihráča počas hry. Môže napríklad sledovať, koľkokrát protihráč zradil v minulosti, a prispôsobiť svoje správanie podľa toho.

    Generous Tit for Tat: Táto stratégia je podobná “Tit for Tat”, ale občas odpustí zradu a pokračuje v spolupráci.

"""
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
    copy_last_very_agressive

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
