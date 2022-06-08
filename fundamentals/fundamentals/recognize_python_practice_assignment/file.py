num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # varial declarations, string, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary of variables, initialize
fruit = ('blueberry', 'strawberry', 'banana') # tuple of variables
print(type(fruit)) # access all elements in tuple
print(pizza_toppings[1]) # access sausage in pizza toppings list
pizza_toppings.append('Mushrooms') #add value in list of pizza toppings
print(person['name']) #should print John in dictionary
person['name'] = 'George' # change value from John to George
person['eye_color'] = 'blue' # add value to dictionary
print(fruit[2]) # access value in tuple, should print banana

if num1 > 45: # conditional check should print It's lower
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # length check  should print It's a long word
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop to stop at 5 index
    print(x)
for x in range(2,5): # for loop to start at 2 index and stop at 5 index
    print(x)
for x in range(2,10,3): # for loop to start at 2 index, stop at 10 index, go by 3 index increments
    print(x)
x = 0
while(x < 5): # whie loop stops at 5
    print(x)
    x += 1 # add increment of 1

pizza_toppings.pop() #remove value from pizza topping list, should remove the last element, olives
pizza_toppings.pop(1) # remove value, should remove the element in the 1 index, sausage

print(person)
person.pop('eye_color') #remove eye color from dictionary
print(person)

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #break loop

def print_hello_ten_times(): #function
    for num in range(10): #parameter
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # function
    for num in range(x): # parameter
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function with argument of variable
    for num in range(x): # parameter
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)  NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'