# 1. Basic

for i in range(151):

    print(i)

# 2. Multiples of Five

for x in range(5,1001):
    if x % 5 ==0:
        print(x)

# 3. Counting, the Dojo Way

for y in range(1,101):
    if y % 10 == 0:
        print('Coding Dojo')
    elif y % 5 == 0:
        print('Coding')
    else:
        print(y)

# 4. Whoa. That Sucker's Huge

odd_number = 0

for a in range(500000):
    if a % 2 != 0:
        odd_number = odd_number + a

print(odd_number)

# 5. Countdown by Fours

for g in range(2018,0,-4):
    if g % 2 == 0:
        print(g)

# 6. flexible counter

low_num = 2
high_num = 30
mult = 5

for z in range(low_num,high_num+1):
    if z % mult == 0:
        print(z)

