#generate a random integer between 1 and 100
import random
jackpot = random.randint(1, 100)
guess = int(input('guess karo'))
counter=1
while guess!=jackpot:
    if guess<jackpot:
        print("wrong!! guess higher")
    else:
        print("wrong!!guess lower")
    guess = int(input('guess karo'))
    counter+=1
else:
    print("Now you are correct!!")
    print("Total attempts = ",counter)


