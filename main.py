import csv
from data import data
rows = []

with open("data.csv", "r", encoding="UTF-8") as f:
    reader = csv.reader(f)

    for row in reader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

final = []

for star_data in star_data_rows:
    distance = star_data[2]

    if len(star_data) == 13:
        gravity = star_data[12]
        distance = distance.replace(",", "")
        data_to_add = {'name': star_data[1][0].upper() + star_data[1:], 'distance':  star_data[2], 'mass':  star_data[3], 'radius':  star_data[4], 'gravity':  star_data[12]}

        if distance and gravity:
            star_data[12] = float(gravity) / 1000
            data_to_add['gravity'] = gravity
            
        final.append(data_to_add)

print(final)
