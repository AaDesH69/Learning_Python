#This is string
#f_name = "Aadesh"
#THis is integer
#num = 20
#This is float
#num1 = 20.5
#This is boolean
#is_true = True

#a = 122
#b = 2121
#print(a + b)

#print(type(f_name))
#print(type(num))
#print(type(num1))
#print(type(is_true))

#To take user input 
#f_name = input("Enter Your Full Name: ")
#print("Your name is " + f_name )
#age = input("Enter Your Age: ")
#print("Your age is " + str(age))

#program to calculate the age by date of birth
#birth_year = input("Enter you year of birth: ")
##current_year = input("What is the current year: ")
#age = int(current_year) - int(birth_year)
#print("Your Current Age is: " + str(age))

#Using conditions
#if age < 18: 
#    print("You are not eligble to enter")
#else:
#    print("You are eligble to enter")
    
#Loops
#for i in range(1, 11):
#    print(i)

""" fruits = ('Mango', 'kera', 'suntala')
if 'kera' in fruits:
    print("There is the element.")
for fruit in fruits:
    print(fruit) """

""" while True:
    per = float(input("Enter Your Percentage: "))
    if per > 80:
        print("You Got 20% Discount")
    else:
        print("You Don't Have Discount") """


""" #Marks Generate Garney Program
print("\t \t \t This is Marks Generator ")

#Showing User other information about marks
#generator

#To show anything in written format using print()
print("\t \t \t Created By Aadesh Pokharel ")

#taking input of marks from the user
science = input("Enter your marks in Science: ")
social = input("Enter your marks in social: ")
nepali = input("Enter your marks in nepali: ")
gk = input("Enter your marks in gk: ")
math = input("Enter your marks in math: ")

#calculating total marks 
totalMarks = float(science) + float(social) + float(nepali) + float(gk) + float(math)
print("Your Marks In Total is: " + str(totalMarks))

#converting total marks into percentage
per = (totalMarks / 500) * 100

print("Your Obtained Percentage is: " + str(per))

if per > 80:
    print("You Have Obtained A+ grade.")
elif per > 70 and per < 80:
    print("You Have Obtained A grade.")
elif per > 60 and per < 70:
    print("You Have Obtained B+ grade.")
elif per > 50 and per < 60:
    print("You have Obtained B grade.")
elif per > 40 and per < 50:
    print("You Have Obtained C+ grade.")
elif per > 30 and per < 40:
    print("You Have Obtained C grade.")
else:
    print("You Are Not Graded.") """

""" #how to identify if a number is odd or even

num = int(input("Enter any Number: "))

if num % 2 == 0:
    if num < 100:
        print(f"{num} is Less Than 100")
    print(f"Given {num} is an Even Number")
else:
    print(f"Given {num} is an Odd Number")
 """

"""
#Program to create pyrimid
 def create_pyramid(rows, symbol="*"):

  pyramid = []
  for i in range(1, rows + 1):
    # Calculate the number of symbols for the current row
    num_symbols = i * 2 - 1
    # Create a centered string with the specified number of symbols
    row = symbol * num_symbols
    centered_row = row.center(rows * 2 - 1)
    pyramid.append(centered_row)
  return pyramid

# Example usage with asterisks
rows = 5
pyramid = create_pyramid(rows)
for row in pyramid:
  print(row)

# Example usage with numbers
rows = 4
number_pyramid = create_pyramid(rows, symbol=str(1))
for row in number_pyramid:
  print(row) """

""" num = 5
for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print("") """

""" #LIST IN PYTHONS 
dep_list = ['Mango', 'Apple']

print(dep_list)

while True:
    del_fruits = input("Enter Fruit you want to delete In Store: ")
    dep_list.remove(del_fruits)
    print(dep_list) """


""" print("\t\t Welcome to DEpartmental Store")

#Creating limit to manupulate in the store
#The List is user Can Only Add or Deleete  from DEpartment 10 times
limit = 10

while True:
    #Empty List
    fruits = ['Apple' , 'Banana', 'Grapes']
    print("\t\t--Add Fruits to Department Store Or Delete Fruits From The Store--")
    print("\t\t--Enter 1 To Add Item and 2 To Delete Item--")
    choose = input("Choose The Option: ")
    item = input("Enter Fruit Name: ")
    
    if int(choose) == 1:
        fruits.append(item)
    elif int(choose) == 2:
        fruits.remove(item)
    print(fruits) """

""" #Departmental Store Example In Python
fruits = []  # List to store fruits

def add_fruit(fruit):
  if len(fruits) < 10 and fruit not in fruits:
    fruits.append(fruit)
    print(f"{fruit} added to the store!")
    return True
  else:
    if len(fruits) == 10:
      print("The store is full, cannot add more fruits!")
    else:
      print(f"{fruit} is already in the store!")
    return False

def delete_fruit(fruit):
  if fruit in fruits:
    fruits.remove(fruit)
    print(f"{fruit} removed from the store!")
    return True
  else:
    print(f"{fruit} is not available in the store!")
    return False

def list_fruits():
  if fruits:
    print("Fruits in the store:")
    for fruit in fruits:
      print(fruit)
  else:
    print("The store is currently empty!")

# Main program loop
while True:
  print("\nFruits Department Store")
  print("1. Add Fruit")
  print("2. Delete Fruit")
  print("3. List Fruits")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    fruit_name = input("Enter fruit name: ")
    add_fruit(fruit_name.lower())  # Convert to lowercase for case-insensitive matching
  elif choice == '2':
    fruit_name = input("Enter fruit name to delete: ")
    delete_fruit(fruit_name.lower())
  elif choice == '3':
    list_fruits()
  elif choice == '4':
    print("Exiting the store!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")
 """
""" for i, j in user_info.key():
    print(i, j)
user_info = {
    'model' : 2008,
    'color' : 'black',
    'price' : 10000,
    'year' : 2008,
    'make' : 'Toyota',
    'type' : 'Sedan'
    }
user_info.update(
    {
        'model' : 2010,
    }
)
print(user_info['model'])
print(user_info) """

""" def create_car_dictionary():
  car_info = {}
  car_info["brand"] = input("Enter car brand: ")
  car_info["model"] = input("Enter car model: ")
  car_info["year"] = int(input("Enter car year: "))
  car_info["color"] = input("Enter car color: ")
  return car_info

# Create the car dictionary
car = create_car_dictionary()

# Print the car information
print("\nCar Details:")
for key, value in car.items():
  print(f"{key.capitalize()}: {value}") """

""" def create_dictionary():
  return {}

def add_word(english_word, nepali_word, dictionary):
  if english_word.lower() not in dictionary:
    dictionary[english_word.lower()] = nepali_word
    print(f"Word '{english_word}' added to the dictionary!")
  else:
    print(f"Word '{english_word}' already exists in the dictionary.")

def translate(english_word, dictionary):
  nepali_word = dictionary.get(english_word.lower())
  if nepali_word:
    return nepali_word
  else:
    return "Word not found"

# Create the empty dictionary
english_nepali_dict = create_dictionary()

# Main program loop
while True:
  print("\nEnglish-Nepali Dictionary")
  print("1. Add Word")
  print("2. Translate English to Nepali")
  print("3. Exit")

  choice = input("Enter your choice (1-3): ")

  if choice == '1':
    english_word = input("Enter English word: ")
    nepali_word = input("Enter Nepali translation: ")
    add_word(english_word, nepali_word, english_nepali_dict)
  elif choice == '2':
    english_word = input("Enter English word to translate: ")
    nepali_translation = translate(english_word, english_nepali_dict)
    print(f"Translation: {nepali_translation}")
  elif choice == '3':
    print("Exiting the program!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 3.")

 """
""" #Sets
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) """

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) 