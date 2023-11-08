# Nested if-else statement to compare the values of amount1 and amount2
amount1 = 20
amount2 = 70

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(f"The greater amount is: {amount1}")
        else:
            print(f"The greater amount is: {amount2}")
    else:
        print("amount2 is not less than 100")
else:
    print("amount1 is not greater than 10")