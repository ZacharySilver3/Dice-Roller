## Random number generator. 
import random
## Lets roll a 6 sided dice and count how many tried it took to reach 6
counter = 0
while True:
    try:
        high = int(input("What number dice do you want to roll?"))
        if high < 1:
            print(f"A dice can not have {high} sides. Please enter a positive number")
        else:
            break
    except ValueError:
        print("Please enter a valid number")
while True:
    try:
        stop = int(input(f"{high} sided dice has been selected. What number do you want to roll to?"))
        if stop < 1:
            print(f"{stop} is not a positive number. Please enter a positive number")
        elif high<stop:
            print(f"{stop} is not on a {high} sided dice. Please enter a number on the dice")
        else:
            break
    except ValueError:
        print("Please enter a valid number")
while True:
    number = random.randint(1,high)
    counter +=1
    if number == stop:
        print(f"{stop} has been rolled and it took {counter} rolls")
        break
    
