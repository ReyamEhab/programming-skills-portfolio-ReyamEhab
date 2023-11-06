# Assuming numbers1 has 100 elements and numbers2 is an empty list
numbers1 = list(range(100))  
numbers2 = []  
# Copying the values from numbers1 to numbers2 using a for loop
for num in numbers1:
    numbers2.append(num)
# Display the contents of numbers2 to verify the copy
print(numbers2)