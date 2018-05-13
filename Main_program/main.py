import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from elo_functions import expected
from elo_functions import elo
import time
import sys


start_time = time.time()


def import_players_csv():
    try:
        temp_df = pd.read_csv("../Data/players.csv")
        print("Imported " + str(temp_df.shape[0]) + " players")
        return temp_df
    except:
        print("--------------------------------")
        print("!!!!! Failed to import players.csv !!!!!")
        print("--------------------------------")


def import_matches_csv():
    try:
        temp_df = pd.read_csv("../Data/matches_season_23.csv")
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


def make_plott_df(players_df):
    temp_df = players_df.set_index("first_name").T
    temp_df["time"] = 0
    temp_df = temp_df.reset_index()
    append_df = pd.DataFrame([["2017-09-08"]], columns=["time"])
    temp_df = temp_df.append(append_df)
    temp_df = temp_df.iloc[-1:]
    return temp_df


def calculate_elo_from_all_matches(elo_df, plott_df):
    stop_flag = 0
    biggest_upset_win_increase = 0
    biggest_upset_loss_decrease = 0
    biggest_upset_player_win = ""
    biggest_upset_player_loss = ""
    biggest_upset_player_date = ""
    last_date = matches_df.iloc[0]['timestamp']

    length = matches_df.shape[0]
    print("Number of matches: " + str(length) + "\n")
    for i in range(length):
        match = matches_df.iloc[i]
        # print(str(i) +": " + str(match['Player 1']) + " - " + str(match['Player 2']))
        player_1 = match["Player 1"]
        player_2 = match["Player 2"]
        elo_rating_a = elo_df[elo_df['first_name'] == player_1]['elo']
        elo_rating_b = elo_df[elo_df['first_name'] == player_2]['elo']

        if (elo_rating_a.shape[0] == 0):
            print("========================================================================")
            print("Player named '" + str(player_1) + "' is NOT FOUND in the player database. ")
            print("========================================================================")
            stop_flag = 1
            continue
        if (elo_rating_b.shape[0] == 0):
            print("========================================================================")
            print("Player named '" + str(player_2) + "' is NOT FOUND in the player database. ")
            print("========================================================================")
            stop_flag = 1
            continue
        elo_rating_a = int(elo_rating_a.values[0])
        elo_rating_b = int(elo_rating_b.values[0])

        if (match['Winner'] == player_1):
            winner_a = 1
            winner_b = 0
        else:
            winner_a = 0
            winner_b = 1
        expected_a = expected(elo_rating_a, elo_rating_b)
        expected_b = expected(elo_rating_b, elo_rating_a)

        new_elo_a = elo(elo_rating_a, expected_a, winner_a, k=50)
        new_elo_b = elo(elo_rating_b, expected_b, winner_b, k=50)

        if new_elo_a - elo_rating_a > biggest_upset_win_increase:
            # New biggest upset detected
            biggest_upset_win_increase = round(new_elo_a - elo_rating_a, 2)
            biggest_upset_loss_decrease = round(elo_rating_b - new_elo_b, 2)
            biggest_upset_player_win = player_1
            biggest_upset_player_loss = player_2
            biggest_upset_player_date = match["timestamp"]
        elif new_elo_b - elo_rating_b > biggest_upset_win_increase:
            # New biggest upset detected
            biggest_upset_win_increase = round(new_elo_b - elo_rating_b, 2)
            biggest_upset_loss_decrease = round(elo_rating_a - new_elo_a, 2)
            biggest_upset_player_win = player_2
            biggest_upset_player_loss = player_1
            biggest_upset_player_date = match["timestamp"]

        # print("New elo a: " + str(new_elo_a))
        # print("New elo b: " + str(new_elo_b))
        # print("Player 1: '" + player_1 + "'. Old elo: " + str(elo_rating_a) + "'. New elo: " + str(new_elo_a) + ". exp: " + str(expected_a) + " " )
        # print("Player 1: '" + player_2 + "'. Old elo: " + str(elo_rating_b) + "'. New elo: " + str(new_elo_b) + ". exp: " + str(expected_b) + " " )
        elo_df = elo_df.set_index('first_name')
        elo_df = elo_df.set_value(player_1, 'elo', new_elo_a + 1)
        elo_df = elo_df.set_value(player_2, 'elo', new_elo_b + 1)
        elo_df = elo_df.reset_index()

        # plotting df updates
        current_date = match['timestamp']
        if last_date == current_date:
            plott_df = plott_df.set_index("time")
            plott_df.set_value(match['timestamp'], player_1, new_elo_a)
            plott_df.set_value(match['timestamp'], player_2, new_elo_b)
            plott_df = plott_df.reset_index()
        else:
            append_df = pd.DataFrame([[match['timestamp']]], columns=["time"])
            plott_df = plott_df.append(append_df)
            plott_df = plott_df.set_index("time")
            plott_df.set_value(match['timestamp'], player_1, new_elo_a)
            plott_df.set_value(match['timestamp'], player_2, new_elo_b)
            plott_df = plott_df.reset_index()
            last_date = current_date

    if(stop_flag):
        sys.exit()

    plott_df = plott_df.fillna(method="ffill")
    length = matches_df.shape[0]
    for i in range(length):
        match = matches_df.iloc[i]
        # print(str(i) +": '" + str(match['Player 1']) + "' - '" + str(match['Player 2']) + "'")
        player_1 = match["Player 1"]
        player_2 = match["Player 2"]
        old_number_of_matches_played_player_1 = elo_df[elo_df['first_name'] == player_1]['matches_played']
        old_number_of_matches_played_player_2 = elo_df[elo_df['first_name'] == player_2]['matches_played']
        if (match['Winner'] == player_1):
            old_number_of_wins_player_1 = elo_df[elo_df['first_name'] == player_1]['wins']
            old_number_of_losses_player_2 = elo_df[elo_df['first_name'] == player_2]['losses']
            elo_df = elo_df.set_index('first_name')
            elo_df = elo_df.set_value(player_1, 'wins', old_number_of_wins_player_1 + 1)
            elo_df = elo_df.set_value(player_2, 'losses', old_number_of_losses_player_2 + 1)
            elo_df = elo_df.reset_index()
        else:
            old_number_of_wins_player_2 = elo_df[elo_df['first_name'] == player_2]['wins']
            old_number_of_losses_player_1 = elo_df[elo_df['first_name'] == player_1]['losses']
            elo_df = elo_df.set_index('first_name')
            elo_df = elo_df.set_value(player_2, 'wins', old_number_of_wins_player_2 + 1)
            elo_df = elo_df.set_value(player_1, 'losses', old_number_of_losses_player_1 + 1)
            elo_df = elo_df.reset_index()

        elo_df = elo_df.set_index('first_name')
        elo_df = elo_df.set_value(player_1, 'matches_played', old_number_of_matches_played_player_1 + 1)
        elo_df = elo_df.set_value(player_2, 'matches_played', old_number_of_matches_played_player_2 + 1)
        elo_df = elo_df.reset_index()
    players = elo_df['first_name']
    for player in players:
        # print(player)
        wins = elo_df[elo_df['first_name'] == player]['wins']
        losses = elo_df[elo_df['first_name'] == player]['losses']
        matches_played = elo_df[elo_df['first_name'] == player]['matches_played']
        if matches_played.values[0] > 0:
            win_rate = round((wins / matches_played) * 100, 4)
            # print(win_rate)
            elo_df = elo_df.set_index('first_name')
            elo_df = elo_df.set_value(player, 'win_rate', win_rate)
            elo_df = elo_df.reset_index()

    return elo_df, plott_df


def make_ordered_elo_ladder(elo_df):
    latex_df = elo_df.sort_values('elo', ascending=False)[
        ['first_name', 'elo', ' joined_date', "matches_played", "wins", "losses", "win_rate"]]
    latex_df.columns = ["name", "elo", "joined_date", "matches_played", "wins", "losses", "win_rate"]
    latex_df = latex_df.reset_index()
    latex_df.index += 1
    latex_df = latex_df[['name', 'elo', "joined_date", "matches_played", "wins", "losses", "win_rate"]]
    latex_df_2 = latex_df.iloc[-5:]
    static_index = latex_df.shape[0] - 4
    elo_limit = latex_df.iloc[static_index - 2]['elo']  # -2 since I set of index
    # print(elo_limit)
    # print(static_index)
    latex_df_2 = latex_df_2.reset_index()
    latex_df_2 = latex_df_2[['name', 'elo', "joined_date", "matches_played", "wins", "losses", "win_rate"]]
    latex_df_2['static_index'] = static_index
    latex_df_2 = latex_df_2[
        ['static_index', 'name', 'elo', "joined_date", "matches_played", "wins", "losses", "win_rate"]]
    latex_df_2['elo'] = "< " + str(elo_limit)
    latex_df = latex_df.iloc[:-5]
    return latex_df, latex_df_2


def clean_elo_df_from_players_with_zero_matches(df):
    df = df[df['matches_played'] > 0]
    return df

def clean_plot_df_from_players_with_zero_matches(df):
    df = df.dropna(1, how='all')
    return df




if __name__ == '__main__':
    print("Welcome to IPK-NTNU-Table-Tennis-Elo-Ladder python script")
    matches_df = import_matches_csv()
    players_df = import_players_csv()
    elo_df = make_elo_df(players_df)
    # elo_df = clean_df_from_players_with_zero_matches(elo_df)
    plott_df = make_plott_df(players_df)

    elo_df, plott_df = calculate_elo_from_all_matches(elo_df, plott_df)
    elo_df = clean_elo_df_from_players_with_zero_matches(elo_df)
    plott_df = clean_plot_df_from_players_with_zero_matches(plott_df)

    elo_df.to_csv("full_elo_ladder.csv")

    plott_df.to_csv("../Data/plot_df.csv")
    ordered_ladder_df, ordered_ladder_df_2 = make_ordered_elo_ladder(elo_df)
    ordered_ladder_df.to_csv("ordered_elo_df.csv")
    ordered_ladder_df_2.to_csv("ordered_elo_df_2.csv")

    end_time = time.time()
    print("Finished script in %s seconds" % (end_time - start_time))
