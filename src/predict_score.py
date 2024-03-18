from dataset import dataset_dictionary, Player
import pprint

def predict_player(season, id):
    
    # add all player entries from dataset dictionary to player dictionary
    player_dictionary = {}
    for temp_season, temp_entry in dataset_dictionary.items():
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

    for prev_season in range(season - season_range, season):
        
        # normalize each stat by games played per season
        gp = player_dictionary[prev_season].games_played
        if gp != 0:
            g = player_dictionary[prev_season].goals / gp
            xg = player_dictionary[prev_season].expected_goals / gp

            a = player_dictionary[prev_season].assists / gp
            
            ppg = player_dictionary[prev_season].powerplay_goals / gp
            shg = player_dictionary[prev_season].shorthanded_goals / gp
            special_g = player_dictionary[prev_season].special_goals / gp

            s = player_dictionary[prev_season].shots / gp
            h = player_dictionary[prev_season].hits / gp
            b = player_dictionary[prev_season].blocks / gp

            # TODO decide on best weights for expected and special goals
            predicted_stats.games_played = 82
            predicted_stats.goals += (g + ((xg - g)*0.2) + (special_g*0.5)) * 82/season_range
            predicted_stats.assists += (a) * 82/season_range
            predicted_stats.powerplay_goals += (ppg + (special_g*0.4)) * 82/season_range
            predicted_stats.shorthanded_goals += (shg + (special_g*0.1)) * 82/season_range
            predicted_stats.shots += (s) * 82/season_range
            predicted_stats.hits += (h) * 82/season_range
            predicted_stats.blocks += (b) * 82/season_range
    
    # TODO formula for fantasy score
    predicted_stats.fantasy_score = 3*predicted_stats.goals + 2*predicted_stats.assists + 0.5*predicted_stats.shots + 0.5*predicted_stats.blocks + 0.5*predicted_stats.powerplay_goals + 0.5*predicted_stats.shorthanded_goals

    # NOTE points calculated after rounding in class
    return predicted_stats.round_stats()

def predict_season(season):
    predicted_season = {}
    # get player id's from previous season
    for id in dataset_dictionary[season - 1]:
        predicted_season[id] = predict_player(season, id)
    
    ranking = {}
    # sort predicted_season by points
    for id, stats in predicted_season.items():
        # TODO this deletes duplicate entries so need a different method
        ranking[stats.fantasy_score] = stats

    return ranking