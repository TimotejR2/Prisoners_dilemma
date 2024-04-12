import csv
import os
from config import DATA_FOLDER_PATH, ROUNDS

def get_datafiles_names(folder_path=DATA_FOLDER_PATH):
    """
    Get names of files in a given folder.

    Args:
        folder_path (str): Path to the folder. Default is DATA_FOLDER_PATH.

    Returns:
        list: List of file names.
    """
    # Get a list of files in the folder
    files = os.listdir(folder_path)

    # Return the list of file names
    return files

class Visualisation:
    def __init__(self):
        """
        Initialize the class with player data and calculate scores and wins.
        """
        # Read player data
        self.data = read()
        # Dictionary to store player objects
        self.players = {}

        # Iterate over each game data
        for game_data in self.data:
            # Iterate over each player in a game
            for player in game_data.players:
                # Create player object if it doesn't exist
                if player not in self.players.keys():
                    self.players[player] = Player(player)

            # Calculate scores and wins for each player
            tmp_players_scores = {0: 0, 1: 0}

            for player in game_data.players:
                # Check if player object exists
                if player not in self.players.keys():
                    raise Exception("Player not found: ", player)

                # Calculate scores for each round
                for round in game_data.rounds:
                    score = round[0 if player == game_data.players[0] else 1]
                    score = int(score)
                    tmp_players_scores[0 if player == game_data.players[0] else 1] += score

                    self.players[player].add_score(score)
            # Assign wins based on scores
            if tmp_players_scores[0] > tmp_players_scores[1]:
                self.players[game_data.players[0]].add_win()

            elif tmp_players_scores[0] < tmp_players_scores[1]:
                self.players[game_data.players[1]].add_win()

    def players_average_score_and_wins(self):

        # Sort players by score
        sorted_players = sorted(self.players.items())

        # Open scores.csv in append mode
        with open('scores.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[player_name for player_name, player in sorted_players])

            # Write header if not already written
            if os.path.getsize("scores.csv") == 0:
                
                writer.writeheader()

            # Write scores of players in sorted_players to row with matching name
            row = {player_name: player.score for player_name, player in sorted_players}
            writer.writerow(row)

        with open('wins.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[player_name for player_name, player in sorted_players])

            # Write header if not already written
            if os.path.getsize("wins.csv") == 0:
                
                writer.writeheader()

            # Write scores of players in sorted_players to row with matching name
            row = {player_name: player.wins for player_name, player in sorted_players}
            writer.writerow(row)
                

        return 
        """
        for player_name, player in sorted_players:
            avg_round_score = round(player.score / len(player.score_add_history), 3)
            print(player_name, "average score:", avg_round_score)

        print("------------------------------------------------------------------------")

        # Sort players by wins
        sorted_players = sorted(self.players.items(), key=lambda x: x[1].wins, reverse=True)
        for player_name, player in sorted_players:
            average_wins = round(player.wins / len(player.score_add_history) * ROUNDS, 3)
            print(player_name, "average wins: ", average_wins)
        """

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0
        self.score_add_history = []
    
    def add_score(self, score):
        self.score_add_history.append(score)
        self.score += score
    
    def add_win(self):
        self.wins += 1

class Game_data:
    """
    Class representing the data for a single game.

    Attributes:
        name (str): The name of the game.
        rounds (list): A list of rounds, where each round is represented by a list of player scores.
        players (list): A list of player names.
    """

    def __init__(self, name, rounds):
        """
        Initialize a Game_data object.

        Args:
            name (str): The name of the game.
            rounds (list): A list of rounds, where each round is represented by a list of player scores.
        """
        self.name = name
        self.rounds = rounds
        self.players = []

        # Add players
        for player in self.name.split(' '):
            self.players.append(player)  # Add each player to the players list


def read():
    """
    Read data from csv files and store it in a list of Game_data objects.

    Returns:
        list: A list of Game_data objects.
    """
    # A list to store all the data from the csv files
    strategy_data = []

    # Loop through each file in the data folder
    for file_name in get_datafiles_names():
        data = []

        # Open and read the csv file
        with open(f'{DATA_FOLDER_PATH}/{file_name}', 'r') as file:
            reader = csv.reader(file)

            # Read the strategy name from the first row of the CSV file
            strategy_name = ' '.join(next(reader))

            # Read the rest of the CSV file and store the data in the list
            for row in reader:
                data.append(row)

        # Create a Game_data object with the data and add it to the list
        game_data = Game_data(strategy_name, data)
        strategy_data.append(game_data)

    # Return the list of Game_data objects
    return strategy_data

def main():
    Visualisation().players_average_score_and_wins()
