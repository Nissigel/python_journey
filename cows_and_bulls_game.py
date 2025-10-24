import random
from termcolor import cprint

def generate_number():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])

def get_hint(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def main():
    secret = generate_number()
    attempts = 0
    cprint ('Welcome to Cows and Bulls!', 'magenta')
    cprint ('Guess the 4-digi number (digits are unique).', 'cyan')

    while True:
        guess = input ('Enter your guess: ')
        if len(guess) != 4 or not guess.isdigit():
            cprint ('Enter exactly 4 digits.', 'red')
            continue

        attempts += 1
        bulls, cows = get_hint(secret, guess)
        cprint (f'{bulls} Bulls, {cows} Cows')

        if bulls == 4:
            cprint (f'You guessed it in {attempts} tries! The number was {secret}.', 'green')
            break

if __name__ == '__main__':
    main()