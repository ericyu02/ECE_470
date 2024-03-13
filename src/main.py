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

print(predict(season, args.id))