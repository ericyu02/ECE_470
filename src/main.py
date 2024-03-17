import argparse
import csv
import os

from dataset import dataset_dictionary
from predict_score import predict


parser = argparse.ArgumentParser()
parser.add_argument("season", help="select season to show i.e. 2022-23")
parser.add_argument("id", help="id of player", type=int)
args = parser.parse_args()

season = int(args.season.split("-")[0])

# Player    id
# McDavid   8478402
# Matthews  8479318
# Maka:     8480069
# Trocheck  8476389

print(predict(season, args.id))