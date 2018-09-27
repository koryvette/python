
# create empty list
temperature = []

# append item to list
temperature.append(98.6)
temperature.append(101.6)
temperature.append(99.4)

print(temperature)

primary_dr = ["dr oz", "dr phil"]
er_dr = ["dr pepper", "dr lach"]

# combine lists
all_dr = primary_dr + er_dr

print(all_dr)

# extend lists
primary_dr.extend(er_dr)

# lists of lists
travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print:("Travel_expenses")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}").format(week_number, sum(week)))
    week_number += 1
