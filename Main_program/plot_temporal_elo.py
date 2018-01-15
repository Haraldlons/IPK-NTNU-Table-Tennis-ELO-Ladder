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
from make_leaderboard_pdf import import_ordered_elo_ladder_s

start_time = time.time()

def import_plot_csv():
    try:
        temp_df = pd.read_csv("../Data/plot_df.csv")
        return temp_df
    except:
        print("Failed to retrieve plot_df")
        sys.exit()

def plot_players(players, plot_df, dates):
    plt.close('all')
    height = 19
    width = 38
    fig = plt.figure(figsize=(width, height))
    # figsize=(38,19) for 2189 x 1229 resoltion. Which is perfect for fullscreen


    for player in players:
        if player == "index":
            continue
        plt.plot(dates, plot_df[player], label=player)
    plt.legend(loc='best')

    # ==== Set figure title and labels ====
    fig.suptitle("Temporal ELO plots", fontsize=35)
    plt.xlabel('Time', fontsize=25)
    plt.ylabel('ELO', fontsize=25)
    plt.grid()
    matplotlib.rcParams.update({'font.size': 17})

    # ==== Save file ====
    directory = "../Results/plots/" + time.strftime("%Y.%m.%d") + "/"
    if not os.path.exists(directory):
        print("Making new folder for plots for " + time.strftime("%Y.%m.%d"))
        os.makedirs(directory)
    fig.savefig("../Results/plots/" + time.strftime("%Y.%m.%d") + "/" + str(players.values[:]) + ".png", bbox_inches='tight')
    # ---- Clear

def get_dates(plot_df):
    dates = []
    for date in plot_df["time"]:
        dates.append(datetime.strptime(date, '%Y-%m-%d'))
    return dates

def plot_all_players_in_bulks_of_ten(plot_df, dates):
    number_of_players = plot_df.shape[1]
    for i in range(2, number_of_players, 10):
        k = i + 9
        if k > number_of_players - 1:
            k = number_of_players -1
        plot_players(plot_df.columns[i:k], plot_df, dates)

def plot_top_and_bottom_players(plot_df, dates):
    latex_df, latex_df_2 = import_ordered_elo_ladder_s()
    plot_players(latex_df.iloc[:10]["name"], plot_df, dates)
    plot_players(latex_df_2.iloc[-10:]["name"],plot_df, dates)


if __name__ == '__main__':
    print("Starting plotting script")
    plot_df = import_plot_csv()
    print("Imported plot_df")
    dates = get_dates(plot_df)
    #plot_players(plot_df.columns[20:30], plot_df, dates)
    plot_all_players_in_bulks_of_ten(plot_df, dates)
    plot_top_and_bottom_players(plot_df, dates)

    end_time = time.time()

    print("Finished plotting script in %s seconds" % (end_time - start_time))