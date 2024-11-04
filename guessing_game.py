# Thayer Yang
# 4 NOV 2024
# Guessing Game

from random import randint, shuffle
from time import sleep

numbers = [1,2,3,4,5,6,7,8,9,10]

shuffle(numbers)
secret_num = numbers[randint(0,len(numbers)-1)]

attempts = 0
guessed_correctly = False

print("Welcome to the Guessing Game!")
sleep(.2)
print("I'm thinking of a number between 1 and 10. You have 3 attempts to guess it.")

while attempts < 3 and not guessed_correctly:
    try:
        guess_num = int(input("Guess a number between 1 and 10: "))
        if guess_num >= 1 and guess_num <=10:
            attempts += 1
            if guess_num == secret_num:
                print(f'You guessed correctly! The secret number was {secret_num}! You did it in {attempts} attempts.')
                guessed_correctly = True
            else:
                print(f'The number {guess_num} is not the secret number!')
                sleep(.1)
        else:
            print('Please enter a number between 1 and 10')
            sleep(1)
    except ValueError:
        print("Please enter a number between 1 and 10")
        sleep(1)

sleep(2)
if guessed_correctly:
    print('Good job! Hope to play with you again soon!')
else:
    print(f'The secret number was {secret_num}! Better luck next time!')
            