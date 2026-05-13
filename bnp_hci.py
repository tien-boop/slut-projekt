import csv
import json

#compare = input("country's BNP per capita and HCI")

with open('bnp.csv', 'r') as file:
    reader = list(csv.DictReader(file))

with open('bnp_json.txt', 'w') as jfile:
    json.dump(reader, jfile)

    search = input("Sök land:")
    



    