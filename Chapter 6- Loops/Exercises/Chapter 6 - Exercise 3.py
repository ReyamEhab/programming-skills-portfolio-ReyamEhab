 while True:
    age = input("Please enter your age (enter 'exit' to quit): ")

    if age.lower() == 'exit':
        break

    try:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    except ValueError:
            print("Please enter a valid age or 'exit'.")