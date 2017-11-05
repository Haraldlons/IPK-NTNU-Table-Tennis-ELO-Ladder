import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from elo_functions import expected
from elo_functions import elo

def import_players_csv():
    try:
        temp_df = pd.read_csv("players.csv")
        print("Imported " + str(temp_df.shape[0]) + " players")
        return temp_df
    except:
        print("--------------------------------")
        print("!!!!! Failed to import players.csv !!!!!")
        print("--------------------------------")


def import_matches_csv():
    try:
        temp_df = pd.read_csv("matches.csv")
        print("Imported " + str(temp_df.shape[0]) + " matches")
        return temp_df
    except:
        print("--------------------------------")
        print("!!!!! Failed to import matches.csv !!!!!")
        print("--------------------------------")

def make_elo_df(players_df):
    elo_df = players_df
    elo_df['elo'] = 1000
    elo_df['matches_played'] = 0
    elo_df['wins'] = 0
    elo_df['losses'] = 0
    elo_df['win_rate'] = 0
    return elo_df

if __name__ == '__main__':
    print("Welcome to IPK-NTNU-Table-Tennis-Elo-Ladder python script")
    matches_df = import_matches_csv()
    players_df = import_players_csv()
    elo_df = make_elo_df(players_df)
    
    print("Finished script")