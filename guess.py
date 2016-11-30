# Guess a random number.
# The program will tell you how many times you tried.
import random

minNumber = 1
maxNumber = 100
randomNumber = random.randint(1, 100)

message = "The number you have to guess is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False
time = 0

while not found:
    time = time + 1
    print("Guess what it is?")
    guess = int(input())
    if guess == randomNumber:
        found = True
        print("*****")
    if guess < randomNumber:
        print("Too low")
    if guess > randomNumber:
        print("Too high")


print("You guessed it! It took you " + str(time) + " times.")
