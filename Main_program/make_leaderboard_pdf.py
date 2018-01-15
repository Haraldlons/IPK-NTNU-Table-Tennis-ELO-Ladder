import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from elo_functions import expected
from elo_functions import elo
import time
import os
import sys
from shutil import copyfile

start_time = time.time()

def import_ordered_elo_ladder_s():
    try:
        temp_df = pd.read_csv("ordered_elo_df.csv")
        temp_df.index += 1
    except:
        print("Failed to load 'ordered_elo_df.csv'")
        sys.exit()

    try:
        temp_df_2 = pd.read_csv("ordered_elo_df_2.csv")
        temp_df_2.index += 1

    except:
        print("Failed to load 'ordered_elo_df_2.csv'")
        sys.exit()

    return temp_df, temp_df_2

def save_to_latex_files(df, df_2):
    directory = "../Results/leaderboard_in_latex/" + time.strftime("%Y.%m.%d") + "/"
    if not os.path.exists(directory):
        print("Making new folder for latex-files for " + time.strftime("%Y.%m.%d"))
        os.makedirs(directory)
        copyfile("../Results/leaderboard_in_latex/template/main.tex", directory+"main.tex")
    df.to_latex("../Results/leaderboard_in_latex/" + time.strftime("%Y.%m.%d") + "/table_1.tex", index=True,
                columns=["name", "elo", "joined_date", "matches_played", "wins", "losses", "win_rate"],
                column_format="|r|l|r|l|l|l|l|l|", longtable=True)
    df_2.to_latex("../Results/leaderboard_in_latex/" + time.strftime("%Y.%m.%d") + "/table_2.tex", index=False,
                  columns=["static_index", "name", "elo", "joined_date", "matches_played", "wins", "losses",
                           "win_rate"], column_format="|r|l|r|l|l|l|l|l|", longtable=True)


if __name__ == '__main__':
    print("Starting script")
    df, df_2 = import_ordered_elo_ladder_s()
    save_to_latex_files(df, df_2)


    end_time = time.time()
    print("Finished script in %s seconds" % (end_time - start_time))