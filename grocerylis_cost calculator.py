#interesting idea posted from reddit...I can make this much better--challenge!
#This proram the user (me) inputs their grocery list prior to going shopping, and is able to veiw an estimate of the total stores.  This program assumes they are shopping from the same stores each week.  A dictionary containing items and their prices I believe is important to use in this program.  I am willing to input all my own weekly grocery items alogn with their costs.#




#Check to see if key exists in dictionary
#add key and value to dicitonary
from itertools import repeat

grocery_index = {"instant oatmeal": 2.49, "buffalo chicken tenders": 6.23, "banza pasta shells": 3.00, "spoon roast": 25.00, "chia seeds": 4.99, "olive oil": 7.49, "mini peppers": 3.99,  "balsamic vinegar": 2.29,  "vitamin d": 4.99, "almonds": 5.99, "riced cauliflower": 1.99, "rice": 4.49, "frozen blueberries": 2.49,
"chicken breasts": 9.79, "eggs": 3.79, "gf bread": 4.49, "grassfed milk": 4.99, "kerrygold butter": 3.49, "carrots": .89, "dish soap": 2.99,
"honey": 5.99, "potatos": 3.49, "celery": 2.69, "red onion": .99, "bag of onions": 2.99, "onion": .69, "tomatos": 2.99, "artichoke hearts": 2.49,
"multivitamin": 11.99, "jalapeno peppers": 1.69,"gf chicken nuggets": 3.69, "mandarins": 3.29, "lemon": .39, "asparagus": 2.29, "avocado": 1.49, "salmon": 9.39,
"iceberg lettuce": 1.69, "whole chicken": 15.22, "hummus": 3.69, "garlic": 3.18, "snow peas": 2.49, "kale": 3.69, "bananas": 1.75,
"heavy cream": 2.29, "peppers": 3.99, "mini cucumbers": 1.99, "beef broth": 2.49, "broccoli": 2.49, "ground beef": 6.99,
"chicken pot pie": 11.99, "baby spinach": 5.29, "pepper jack cheese": 2.5, "df ice cream": 4.69, "hard goat chedder": 2.99,
"kefir": 2.99, "cottage cheese": 2.39, "milk": 1.79, "raos sauce": 8.99, "chick pea pasta": 2.5, "dark chocolate chips": 4.99,
"banza pasta shells": 3.49, "gatorade powder": 2.99, "macaroni and cheese": 2.59, "breakfast sausage": 2.5, "df butter": 4.39,
"true lemon": 2.00, "tea tree soap": 4.99, "paper towels": 12.99}

#I open the program and am assined a list for input
my_list=[]

#Havent purchased anything yet
cost = []

#function to view their total cost
def grocery_total(grocery_index, my_list, cost):
  while True:

    for x in my_list:

        if x in grocery_index.keys():
            cost.append(grocery_index[x])

        elif x not in grocery_index:

            break
    amount = (sum(cost))
    print(f"${amount}")
    prompt = input("Enter 'quit' to exit")
    if prompt == 'quit':
        return cost

# function to veiw or remove items from their list
def grocery_list(my_list, grocery_index):
  while True:
    print(my_list)
    prompt = input("Enter 'remove' to remove an item or 'quit' to return\n")
    if prompt == 'quit':
      return my_list
    elif prompt == 'remove':
      while True:
        item_removal = input("Enter an item to remove, or 'quit' to return\n")
        if item_removal == 'quit':
          return my_list
        else:
          my_list.remove(item_removal)
          print(my_list)


#Sets main menu
def main_menu(my_list, grocery_index, grocery_total):

  while True:

    menu = input("Enter\n'list' to view your list\n'input' to add items to your list\n'total' to view your current cost\n")

    if menu == 'input':
      make_a_list(my_list)

    elif menu == 'list':
      grocery_list(my_list, grocery_index)

    elif menu == 'total':
      grocery_total(grocery_index, my_list, cost)
#able to enter amount so I am not typing cottage cheese 5 times. code should add 5 cottage cheeses if I input a qty of 5

#function to make a grocery list
def make_a_list(my_list):
  print("Enter list\nType 'quit' to exit to main menu.\nType 'remove' to remove the last entered item.")
  print("Type 'qty' to input multiple of a single item.")
  print("Type 'search' to verify an item in list.")

  while True:
    unfounded_items = []
    item = input()
    my_list.append(item)

    if item == 'remove':
        my_list.pop() #removes 'remove' from list
        my_list.pop() #removes the last inputted foor from list

    elif item == 'qty':
      my_list.pop()
      item = input("Enter the item\n")
      if item not in grocery_index:
       unfounded_items.append(item)
       print(f"{unfounded_items} not found")
       break
       make_a_list(my_list)
      qty = int(input("Enter the qty\n"))
      my_list.extend(repeat(item,qty))

    elif item == 'search':

      my_list.pop()
      search = input("Type item to search.\n")

      if search in my_list:

        duplicates = my_list.count(search)
        print(f"Yes, {search} has been added {duplicates} time(s).")

      else:
        print(f"No, {search} has not been added.")
      print("Enter items to add to your list.")

    elif item == 'quit':
        my_list.pop() #This line is to remove quit from the list
        return my_list

    elif item not in grocery_index:
      unfounded_items.append(item)
      my_list.pop()
      print(f"Undefined entry\n{unfounded_items}")

      #Should be a function asking yes/no whether or not to add inputted item and price.

#calls main menu.
main_menu(my_list, grocery_index, grocery_total)
