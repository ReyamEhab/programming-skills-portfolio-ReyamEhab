guests = ['Kamal', 'Ahmed', 'Mariam', 'fatima']
name = guests[0]
print(name+ ", please come to dinner.")

name = guests[1]
print(name + ", please come to dinner.")

name = guests[2]
print(name+ ", please come to dinner.")

name = guests[3]
print(name+ ", please come to dinner.")

name = guests[1]
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Maha')

name = guests[0]
print("\n" + name + ", please come to dinner.")

name = guests[1]
print(name + ", please come to dinner.")

name = guests[2]
print(name + ", please come to dinner.")

name = guests[3]
print(name + ", please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

 
 

