# 1. Update Values in Dictionaries and Lists
    # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    # 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
    # 3. In the sports_directory, change 'Messi' to 'Andres'
    # 4. Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# ANSWER 1.1

x[1][0] = 15
print(x)

# ANSWER 1.2

students[0]['last_name'] = 'Bryant'
print(students[0])

# ANSWER 1.3

sports_directory['soccer'][0]= 'Messi'
print(sports_directory['soccer'])

# ANSWER 1.4

z[0]['y']= 30
print(z)

# 2. Iterate Through a List of Dictionaries
    # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in some_list:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
    # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# 4. Iterate Through a Dictionary with List Values
    # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print("")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

printInfo(dojo)









