def greeting():
    x = "Welcome"
    print(x)


# greeting()

# two parameters, phrase, num of times we want to repeat it
# welcome sal, 3

def repeat_phrase(phrase, times_to_repeat):
    # print(phrase*times_to_repeat)
    for i in range(times_to_repeat):
        print(phrase)
repeat_phrase("Welcome sal", 3)

def number_list(number):
    my_list = []
    for i in range(number):
        my_list.append(i)
    return my_list

print(number_list(10))