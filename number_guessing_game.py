import random

numToGuess = random.randint (1, 100)
while True:

    try:
        guess = int (input ('Guess a number between 0 and 100: '))

        if (guess < numToGuess):
            print ('Number is too low. Try again!')
        elif (guess > numToGuess):
            print ('Number is too high. Try again!')
        else:
            print ('Congratulations! You guessed the right number')
            break
    except ValueError:
        print ('Please enter a valid number')