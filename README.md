# NHL Fantasy Score Predictor #
ECE 470 - Artificial Intelligence
* Cameron Fietz
* Benjamin Philipenko
* Eric Yu

## REQUIREMENTS
Python3 \
numpy \
scikit-learn 

To install all dependencies:\
`pip3 install -r requirements.txt`

----

## How to use:
Ensure you are in the src/ directory.

### Find unqiue player id
- Replace `'player_name'` with the name of the player you want to get the id for.
- Name cannot have spaces so pick first or last name \
`py ./dataset.py 'player_name'` 

### Get Fantasy Score Prediction 
- Replace `'season'` with the season you want to predict (ie. 2022-23.)
- Enter `'all'` to predict all player fantasy scores or replace `'player_id'` to predict a specific player's fantasy score. \
All players: `py main.py 'season' 'all'` \
Specific Player: `py main.py 'season' 'player_id'`