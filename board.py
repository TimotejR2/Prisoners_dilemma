import csv
import os
from config import COOPERATE, DEFECT, DATA_FOLDER_PATH
from config import COOP_COOP, COOP_DEF, DEF_COOP, DEF_DEF

class Board:
    """
    Class that simulates the game board.
    """
    def __init__(self):
        """
        Initialize the game state variables including moves, max_score, min_score, and score_list.
        """
        self.moves = [] # List of moves that have been made
        self.max_score = 0 # Score of max player
        self.min_score = 0 # Score of min player
        self.score_list = [] # List of scores that has been added after every round

    def make_move(self, max_player_move, min_player_move):
        """
        Adds the moves made by the players to the list of moves and updates the scores.
        
        Parameters:
            max_player_move (int): The move made by the maximum player.
            min_player_move (int): The move made by the minimum player.
        
        Returns:
            None
        """

        self.moves.append([max_player_move, min_player_move])

        scores = {
            (COOPERATE, COOPERATE): COOP_COOP,
            (COOPERATE, DEFECT): COOP_DEF,
            (DEFECT, COOPERATE): DEF_COOP,
            (DEFECT, DEFECT): DEF_DEF
        }

        score = scores[(max_player_move, min_player_move)]
        self.max_score += score[0]
        self.min_score += score[1]
        self.score_list.append(score)

    def clear(self):
        """
        Clears the moves, max_score, min_score, and score_list attributes of the object.
        """
        self.moves = []
        self.max_score = 0
        self.min_score = 0
        self.score_list = []

    def write(self, max_name, min_name):
        """
        Write the scores of the game to a CSV file.

        Args:
            max_name (str): The name of the first player.
            min_name (str): The name of the second player.
        Returns:
            None
        """
        # create folder if it doesn't exist with name as variable DATA_FOLDER_PATH
        os.makedirs(DATA_FOLDER_PATH, exist_ok=True)

        with open(f'{DATA_FOLDER_PATH}/{max_name}_{min_name}.csv', mode='w', newline='') as file:
            # Remove all data from file
            file.truncate(0)

            # Write header and all rounds scores
            writer = csv.writer(file)
            writer.writerow([max_name, min_name])
            for line in self.score_list:
                writer.writerow(line)


    def get_score(self):
        """
        Calculate and return the score difference between the maximum score and the minimum score.
        """
        return self.max_score - self.min_score

    def get_all_score(self):
        """
        Return all scores
        """
        return self.max_score, self.min_score

    def get_moves(self):
        """
        Return all moves made.
        """
        return self.moves
    