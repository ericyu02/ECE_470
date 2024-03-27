from dataset import dataset_dictionary, Player
import numpy as np
import pprint

def predict_player(season, id):
    # add all player entries from dataset dictionary to player dictionary
    player_dictionary = {}
    for temp_season, temp_entry in dataset_dictionary.items():
        if temp_season < season:
            if id in temp_entry:
                player_dictionary[temp_season] = temp_entry[id]

    # pad dictionary with empty stats for missing years
    min_season = min(player_dictionary.keys())
    max_season = max(player_dictionary.keys())
    for temp_season in range(min_season, max_season):
        if (temp_season not in player_dictionary):
            player_dictionary[temp_season] = Player(id=id, season=temp_season, name=player_dictionary[min_season].name, team='N/A', position='N/A')
    #pprint.pprint(player_dictionary)
            
    # figure out range of seasons to use based on games played
    season_range = 0
    games_played = 0
    threshold_games_played = 200
    cutoff_games_played = 10
    # use dataset until player has enough (200) games played or reached end of dataset
    while (games_played < threshold_games_played) and (season_range < len(player_dictionary)):
        season_range += 1
        games_played += player_dictionary[season - season_range].games_played
    
    # predict player stats 
    predicted_stats = Player(id=id)
    predicted_stats.season = season
    predicted_stats.name = player_dictionary[season - 1].name
    predicted_stats.team = player_dictionary[season - 1].team
    predicted_stats.position = player_dictionary[season - 1].position

    # if there is insufficient data, cannot predict
    if games_played < cutoff_games_played:
        return predicted_stats.round_stats()
    gp = g = xg = a = ppg = shg = special_g = s = h = b = 0
    # get total stats over season range
    for prev_season in range(season - season_range, season):
        # played at least 1 game
        if player_dictionary[prev_season].games_played > 0:
            gp += player_dictionary[prev_season].games_played
            g += player_dictionary[prev_season].goals
            xg += player_dictionary[prev_season].expected_goals

            a += player_dictionary[prev_season].assists
            
            ppg += player_dictionary[prev_season].powerplay_goals
            shg += player_dictionary[prev_season].shorthanded_goals
            special_g += player_dictionary[prev_season].special_goals

            s += player_dictionary[prev_season].shots
            h += player_dictionary[prev_season].hits
            b += player_dictionary[prev_season].blocks

    # normalize stats by dividing by games played and propagating for 82 game season
    # TODO decide on best weights for expected and special goals
    # TODO implement linear regression model
    predicted_stats.games_played = 82
    predicted_stats.goals = (g + ((xg - g)*0.2) + (special_g*0.5)) * 82/gp
    predicted_stats.assists = (a) * 82/gp
    predicted_stats.points = round(predicted_stats.goals) + round(predicted_stats.goals)
    predicted_stats.powerplay_goals = (ppg + (special_g*0.4)) * 82/gp
    predicted_stats.shorthanded_goals = (shg + (special_g*0.1)) * 82/gp
    predicted_stats.shots = (s) * 82/gp
    predicted_stats.hits = (h) * 82/gp
    predicted_stats.blocks = (b) * 82/gp
    
    # formula for fantasy score
    predicted_stats.fantasy_score = 3*predicted_stats.goals + 2*predicted_stats.assists + 0.5*predicted_stats.shots + 0.5*predicted_stats.blocks + 0.5*predicted_stats.powerplay_goals + 0.5*predicted_stats.shorthanded_goals

    # calculate percentage difference between predicted and true fantasy score
    pd = 100
    
    return predicted_stats.round_stats(), pd

def predict_season(season):
    predicted_season = {}
    percentage_difference = []
    # get player id's from previous season
    for id in dataset_dictionary[season - 1]:
        predicted, pd = predict_player(season, id)
        if predicted.fantasy_score > 0:
            predicted_season[id] = predicted
            percentage_difference.append(pd)
    
    ranking = []
    # sort predicted_season by points
    for id, stats in predicted_season.items():
        ranking.append(stats)
    ranking.sort(key=lambda x: x.fantasy_score)
    
    # calculate mean percentage difference between predicted and true fantasy score
    print(percentage_difference)
    mpd = np.mean(pd)

    return ranking, mpd