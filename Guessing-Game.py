import random

comNum = random.randint(0,100)

while True:
    userGuess = int(input('Guess a number between 0 and 100'))
    if userGuess > comNum:
        print('Guess lower')
    elif userGuess < comNum:
        print('Guess higher')
    else:
        print('Congrats! You win!')
    
