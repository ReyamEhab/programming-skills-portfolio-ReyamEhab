# Make several dictionaries
# Make an empty list to store the pets in.
pets = []
pet = {
    'animal type ': 'butterflies',
    'name': 'lucy',
    'owner':'Reyam',
    'weight':1,
    'eats': 'leaves',
}
pets.append(pet)

pet = {
    'animal type ': 'dog',
    'name': 'carlo',
    'owner':'Ehab',
    'weight':6,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type ': 'fish',
    'name': 'lora',
    'owner':'Abrar',
    'weight':2.5,
    'eats': 'beans',
}
pet = {
    'animal type ': 'Penguin',
    'name': 'meme',
    'owner':'Ahmed',
    'weight':5,
    'eats': 'fish',
}
pets.append(pet)
for pet in pets:
    print("\nHere's what i know about" +pet['name'] + "!")
    for key, value in pet.items():
        print("\t" + key + ": "+ str(value))