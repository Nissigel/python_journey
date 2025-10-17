import random
from termcolor import cprint

def roll_die():
    return random.randint(1, 6)

def play_turn(player_name):
    turn_score = 0
    cprint(f"\n🎲 {player_name}'s turn", 'cyan', attrs=['bold'])

    while True:
        roll = roll_die()
        cprint(f'You rolled a {roll}', 'yellow')

        if roll == 1:
            cprint('💀 You rolled a 1! No points this turn.', 'red')
            return 0
        
        turn_score += roll
        cprint(f'Current turn score: {turn_score}', 'magenta')

        choice = input("Roll again? (y/n or 'q' to quit): ").lower()
        if choice == 'q':
            return None
        elif choice != 'y':
            return turn_score

def main():
    scores = [0, 0]
    current_player = 0

    cprint("🎯 Welcome to the Dice Game! First to 100 points wins!\n", 'blue', attrs=['bold'])
    cprint("Type 'q' anytime to quit.", 'red')

    while True:
        player_name = f'Player {current_player + 1}'
        turn_score = play_turn(player_name)

        # 🛑 Handle quit action safely
        if turn_score is None:
            cprint(f"\n🚪 {player_name} decided to quit. Game over!", 'red', attrs=['bold'])
            break

        scores[current_player] += turn_score

        cprint(f'\nYou scored {turn_score} points this turn.', 'cyan')
        cprint('Current scores:', 'white', attrs=['bold'])
        print(f'  🧍 Player 1: {scores[0]}')
        print(f'  🧍 Player 2: {scores[1]}')

        if scores[current_player] >= 100:
            cprint(f'\n🎉 {player_name} wins with {scores[current_player]} points! 🏆', 'green', attrs=['bold'])
            break

        # Switch player
        current_player = 1 - current_player

if __name__ == '__main__':
    main()
