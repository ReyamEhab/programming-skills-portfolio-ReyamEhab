# Get the month input 
month = input("Enter the month ( January, February, march, april, may, june, july, august, september, october, november .): ")
month = month.lower()
if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Autumn"
else:
    season = "Invalid input. Please enter a valid month."
print(f"The season for the month of {month} is {season}.")