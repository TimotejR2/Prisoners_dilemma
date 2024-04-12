import os
import csv
from runner import main as simulate
from visualisation import main as visualise
from visualisation import get_datafiles_names
from config import ROUNDS, DATA_FOLDER_PATH

LINES_TO_REMOVE = 5
def main():
    # Remove wins.csv and scores.csv
    try:
        os.remove('wins.csv')
        os.remove('scores.csv')
    except:
        pass

    simulate()
    visualise()
    all_data_csvs = get_datafiles_names()

    for i in range (0,ROUNDS-LINES_TO_REMOVE,LINES_TO_REMOVE):
        
        print("Rounds: ", ROUNDS-i-LINES_TO_REMOVE)
        for file_name in all_data_csvs:
            remove_last_n_lines(f'{DATA_FOLDER_PATH}/{file_name}', LINES_TO_REMOVE)
        
        visualise()
    reverse_csv('wins.csv')
    reverse_csv('scores.csv')

def reverse_csv(filename):
    """
    Reverse the order of rows in a CSV file.

    Args:
        filename (str): The name of the CSV file.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        rows = rows[1:]
        rows.reverse()
        for row in rows:
            writer.writerow(row)

def remove_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Remove the last n lines
    lines = lines[:-n]

    with open(filename, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()