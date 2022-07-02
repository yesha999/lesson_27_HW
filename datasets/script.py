import csv
import json

with open('categories.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('categories.json', 'w') as f:
    json.dump(rows, f)


with open('ads.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('ads.json', 'w') as f:
    json.dump(rows, f)