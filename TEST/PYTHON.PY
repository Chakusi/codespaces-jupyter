#import os
import csv
import pandas as pd



with open('/workspaces/codespaces-jupyter/TEST/bangalore-rainfall-data-1900-2024-sept.csv', mode ='r')as file:
  csvFile = pd.read_csv(file)
  #csvFile = csv.DictReader(file)
  #for lines in csvFile:
  #      print(lines)
  print(sum(csvFile.Jan))
