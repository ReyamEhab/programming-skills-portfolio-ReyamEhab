#uses the break statement
num = [2,3,4,6,7,8,9]
target_num = 6
for num1 in num:
    print(num1)
    if num1 == target_num:
        print(f"found the target num {target_num}'.exiting the loop")
        break
