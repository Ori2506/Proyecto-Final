import csv
import pandas as pd

with open("C:\Users\Gaby_\Downloads\starwars.zip\csv\starships", "r")as csvfile:
    reader = csv.reader(csvfile)
    data=list(reader)