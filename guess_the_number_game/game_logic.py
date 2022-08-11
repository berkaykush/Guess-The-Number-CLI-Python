from random import randrange
from out_of_bounds_error import OutOfBoundsError

PICKED_NUMBER = randrange(1, 101)


def print_welcome_message():
    print("\nWELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100.")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD.")
    print("If your guess is within 10 of my number, I'll tell you that you are WARM.")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER.")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER.")
    print("LET'S PLAY!\n")


def is_out_of_bounds(num):
    return (num < 1) or (num > 100)


def check_entered_guess():
    while True:
        try:
            entered_guess = int(input('Guess the number between 1 and 100: '))

            if is_out_of_bounds(entered_guess):
                raise OutOfBoundsError

            return entered_guess
        except ValueError:
            print('The given input is not a natural number.\n')
        except OutOfBoundsError:
            print('OUT OF BOUNDS\n')


def is_first_turn(turn):
    return turn == 1


def is_guess_within_10_of_picked_num(guessed_num):
    return abs(guessed_num - PICKED_NUMBER) <= 10


def is_prev_guess_closer_than_current_guess(prev_guess, current_guess):
    return abs(current_guess - PICKED_NUMBER) > abs(prev_guess - PICKED_NUMBER)


def guessing(num_guesses=0, prev_guess=None):
    while True:
        entered_guess = check_entered_guess()
        num_guesses += 1

        if entered_guess == PICKED_NUMBER:
            return num_guesses

        if is_first_turn(num_guesses):
            if is_guess_within_10_of_picked_num(entered_guess):
                print('WARM!\n')
            else:
                print('COLD!\n')
        else:
            if is_prev_guess_closer_than_current_guess(prev_guess, entered_guess):
                print('COLDER!\n')
            else:
                print('WARMER!\n')

        prev_guess = entered_guess


def main():
    print_welcome_message()
    print(f'\nCONGRATULATIONS, YOU GUESSED IT IN ONLY '
          f'{guessing()} GUESSES!!')


if __name__ == '__main__':
    main()
