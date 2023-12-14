from typing import Self
class VendingMacine:
     def __init__(self):
      self.menu = {
               'drinks ☕ ':{
                    'A1':{'name':'Arabian Coffee', 'price': 3.00, 'quantity':5},
                    'A2':{'name':'Cappuccino', 'price': 2.00, 'quantity':10},
                    'A3':{'name':'Coffee', 'price': 1.00, 'quantity':20},
                    'A4':{'name':'Karak tea', 'price': 1.50, 'quantity':5},
            },
            'snakes 🍫 ':{
                'B1':{'name':'Pop corn ', 'price': 1.00, 'quantity':12},
                'B2':{'name':'Dark Chocolate', 'price': 2.00, 'quantity':7},
                'B3':{'name':'Chips', 'price': 4.00, 'quantity':18},
                'B4':{'name':'Cup cake', 'price': 3.50, 'quantity':20},
            },
            'Soft Drinks 🥤 ':{
                'C1':{'name':'Cola', 'price': 3.00, 'quantity':10},
                'C2':{'name':'Fanta', 'price': 4.00, 'quantity':14},
                'C3':{'name':'Orange juice', 'price': 1.00, 'quantity':18},
                'C4':{'name':'Apple juice', 'price': 1.50, 'quantity':20},
            },    
        }
     
     
#define a method to display items in a specified category 
     def display_items(self,category):
          print(f"""
   ___   _   _   _   _   _   _   _   _  
  /   \ / \ / \ / \ / \ / \ / \ / \ / \
 ( W ) ( E ) ( L ) ( C ) ( 0 ) ( M ) ( E )
  \___/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
   ___   _   _   _   _   _   _   _   _  
  /   \ / \ / \ / \ / \ / \ / \ / \ / \
 ( T ) ( O ) (   ) ( M ) ( Y ) (   ) (  )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
   ___   _   _   _   _   _   _   _   _  
  /   \ / \ / \ / \ / \ / \ / \ / \ / \
 ( V ) ( E ) ( N ) ( D ) ( I ) ( N ) ( G )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
   ___   _   _   _   _   _   _   _   _  
  /   \ / \ / \ / \ / \ / \ / \ / \ / \
 ( M ) ( A ) ( C ) ( H ) ( I ) ( N ) ( E )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
    """)
          print("Available Items:")
#Iterate through items in specified category and display their details  
          for code, item in self.menu[category].items():
               print(f"{code}: {item['name']} - 💵 {item['price']:2f} (Qty: {item['quantity']})")
          print("\nyour current balance: 💵 {:.2f}".format(self.balance))
#define a method to insert money into the vending machine 


#Define the method to insert money into the vinding machine
     def insert_money(self):
        while True:
            try:
                    #prompt the user to input the amount of money 
                    amount = float(input("Insert money (enter 0 to cancel):  💵"))
                    #check if the amount is positive 
                    if amount < 0:
                         print("please enter a positive amount.")
                         #check if the user wants to cancel the operation
                    elif amount ==0:
                         break 
                    else:
                         #Update the balance and display the updated balance 
                         self.balance += amount 
                         print ("Balance updated. your current balance:  💵 {:2f}".format(self.balance)) 
                         break
            except ValueError:
                 print("Invalid input. please enter a valid amount.")


    #define a method to purchase an item from the vending machine 
     def purchase_item(self, category, code):
         #check if the item code is valid 
         if code in self.menu[category]:
              #Retrieve the item details 
              item = self.menu[category][code]
              #check if the item is in stock and the balance is sufficient 
              if item['quantity'] > 0 and self.menu >= item['price']:
                   #update the balance, reduce the quantity, and inform the user of the successful purchase 
                   self.balance -= item['price']
                   item['quantity'] -= 1
                   print("You've successfully purchased{}.Enjoy!".format(item['name']))
                #if the item is out of stock, inform the user 
              elif item['quantity']  ==0:
                   print("Sorry, {} is out of stock.".format (item['name']))
                   #if the balance is insufficient, prompt the user to insert more money 
              else:
                   print("Insufficient funds. please try again. ")
         else:
            #if the item code is invalid, please inform the user 
          print("Invalid item code. Please try again. ")


    #define a method to start the vending machine 
     def start(self):
         while True:
              #display the category options to the user 
              print("Select category:")
              print("1. Drinks ☕ ")
              print("2. Snacks 🍫 ")
              print("3. Soft Drinks 🥤 ")
              print("Enter 'exit' to end.")
              #prompt the user to enter thier choice 
              choice = input("Enter your choice 1,2, 3 or 'exit'): ")
              #check the user's choice and set the category accordingly 
              if choice.lower() == 'exit':
                   print("Thank you for using the creative vending machine. Have a great day! ")
                   break 
              elif choice =='1':
                   category = 'drinks'
              elif choice =='2':
                   category = 'Snacks ' 
              elif choice == '3':
                   category = 'Soft drinks' 
              else:
                   print("Invalid choice. Please enter 1,2, 3 or 'exit'.")    
                   continue
              

              #display the items inn the selected category 
              self.display_items(category)
              #Allow the user to insert money 
              self.insert_money()
              #prompt the user to enter the code of the item they want to purchase 
              item_code = input("Enter the code of the item you want to purchase: ")
               #process the purchase based on the selected category and item code 
              self.purchase_item(category, item_code)


#Check if the script is being run as the main program 
if __name__ == "__main__":
     #create a instance of the VendingMachine class
     vending_machine = VendingMacine()
     #start the vending machine 
     vending_machine.start()
                   

 


 
                 
    
