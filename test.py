import json
from tabulate import tabulate

# Wczytaj dane z pliku JSON
with open('database.json') as file:
    data = json.load(file)

# Przekształć dane na listę list
table = []
for item_type, items in data['database'].items():
    for item in items:
        table.append([item['name'], item['price']])

# Wydrukuj tabelę
print(tabulate(table, headers=['Nazwa', 'Cena'], tablefmt='grid'))
