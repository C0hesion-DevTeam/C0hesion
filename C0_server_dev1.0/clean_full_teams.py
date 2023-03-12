import csv

with open('teams_request.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)


indices_to_delete = []
for i, row in enumerate(rows):
    if row['needpeople'] == '0':
        indices_to_delete.append(i)

# Delete the rows in reverse order
for i in reversed(indices_to_delete):
    del rows[i]




with open('teams_request.csv', 'w', newline='') as csvfile:
    fieldnames = ['studentname','teamtype','peoplenum','description','needpeople']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
