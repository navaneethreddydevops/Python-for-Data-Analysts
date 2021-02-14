# IF-ELIF LOOP
i = 35
if i == 35:
    print('i is 35')
elif i == 45:
    print('i is 45')

# IF-ELIF-ELSE LOOP
i = 11
if i == 45:
    print('i is 45')
elif i == 35:
    print('i is 35')
elif i > 10:
    print('i is grater than 10')
elif i % 3 == 0:
    print('i is multiplier by 3')
else:
    print('I dont know much about i')

# For Loops
for i in range(100):
    x = i*2
    print(x)

# For Loop with continue
for i in range(10):
    if i == 3:
        continue
    print(i)

# While Loops
count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

# While Loops with break
count = 0
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1
# Handling exceptions
thinkers = ['plato', 'PlayDo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("we tried to pop too many thinkers")
        print(e)
    break

# Accessing the object data


class FunctionCar():
    wheels = 4

    def driveFast(self):
        print("Driving so fast")


'''
# Instantiate a fancy car
my_car=FunctionCar()
# Access the class attribute
my_car.wheels
# Invoke the method
my_car.driveFast()
'''
# Sequences
2 in [1, 2, 3]

'a' not in 'cat'

10 in range(10)

10 in range(12)

10 not in range(0, 4)

# To get the Index value of specific Value
my_sequence = 'Bill Cheatham'

my_sequence.index('m')
my_sequence.index('C')

my_sequence[start:stop:step]

# it will print out the index value of a specific character

# Squaring the Values on a Range
squares = []
for i in range(10):
    squared = i*i
    squares.append(squared)

# Simple form of Loop
squares = [i*i for i in range(10)]
squares

# Remove the white spaces from a input string

input = " I want more "
input.strip()  '''This will remove both left and right spaces of string'''
input.lstrip() '''This will remove the left side space of input string'''
input.rstrip() '''This will remove the right side space of input string'''


