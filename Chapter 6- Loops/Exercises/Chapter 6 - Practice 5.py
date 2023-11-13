#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.
largest = None 
while True:
   user_input = input ("Enter a number (or '0' to exit the loop:")
   if user_input == '0':
      break
   
   try:
      num = float(user_input)
      if largest is None or num > largest:
         largest = num
   except ValueError:
      print("invalid input.Enter a number (or '0' to exit the loop.")
if largest is not None:
   print("The largest num entred is:" ,largest)
else:
   print("No valid numbers were entered")


