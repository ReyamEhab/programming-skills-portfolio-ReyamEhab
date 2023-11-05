rivers = {
    'nile': 'Sudan',
    'Chelif': 'Algeria',
    'Gash': 'Eritrea',
    'Atbara': 'Ethiopia',
    'Bafing': 'Mali',
    }

for river, country in rivers.items():
    print("The " + river + " flows through " + country + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river)

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country )