import csv
import json

# Для категорий
with open('category.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dictionary_list = []
    pk = 0
    for i in reader:
        pk += 1
        dictionary_list.append({"fields": i, "model": "ads.category", "pk": pk})

with open('../fixtures/category.json', 'w') as f:
    json.dump(dictionary_list, f)

# Для объявлений
with open('ad.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dictionary_list = []
    pk = 0
    for i in reader:
        pk += 1
        dictionary_list.append({"fields": i, "model": "ads.ad", "pk": pk})

with open('../fixtures/ad.json', 'w') as f:
    json.dump(dictionary_list, f)

# Для локаций
with open('location.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dictionary_list = []
    pk = 0
    for i in reader:
        pk += 1
        dictionary_list.append({"fields": i, "model": "users.location", "pk": pk})

with open('../fixtures/location.json', 'w') as f:
    json.dump(dictionary_list, f)

# Для юзеров
with open('user.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dictionary_list = []
    pk = 0
    for i in reader:
        i["location"] = list(i["location"])
        pk += 1
        dictionary_list.append({"fields": i, "model": "users.user", "pk": pk})

with open('../fixtures/user.json', 'w') as f:
    json.dump(dictionary_list, f)
