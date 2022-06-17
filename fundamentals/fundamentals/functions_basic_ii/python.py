# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element). 
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(a,b):
    my_list = []
    for i in range(a,b-1,-1):
        my_list.append(i)
    return my_list

print(countdown(5,0))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second. 
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(some_list):
    print(some_list[0])
    return some_list[1]

print(print_and_return([1,2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length. 
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(some_list):
    return some_list[0] + len(some_list)

print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(some_list):
    if len(some_list) < 2:
        return False
    new_list = []
    for i in range(0,len(some_list)):
        if some_list[i] > some_list[1]:
            new_list.append(some_list[i])
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(a,b):
    my_list = []
    for i in range(0,a):
        my_list.append(b)
    return my_list

print(length_and_value(4,7))
print(length_and_value(6,2))