# Thayer Yang
# 4 NOV 2024
# Range Function

from time import sleep

# 4-3 Counting to Twenty

for number in range(1,21):
    print(number)
    sleep(.25)

# # 4-4 One Million

# numbers = []

# for number in range(1,1000001):
#     numbers.append(number)

# for element in numbers:
#     print(element)
#     #sleep(.01)

# # 4-5 Summing a Million
    
# sum_of_million = sum(numbers)
# print(sum_of_million)

# # 4-6 Odd Numbers

for number in range(1,21,2):
    print(number)
    sleep(.2)

# 4-7 Threes
    
for three in range(3,31,3):
    print(three)
    sleep(.2)

# 4-8 Number Cubes
    
for number in range(1,11):
    print(f'{number} cubed is {number**3}')
    sleep(.2)