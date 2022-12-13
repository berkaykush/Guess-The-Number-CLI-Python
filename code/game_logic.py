import random, os

from out_of_bounds_error import OutOfBoundsError

selected_num = 0


def print_welcome_message():
    print("\nWELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100.")
    print(
        "If your guess is more than 10 away from my number, I'll tell you you're COLD."
    )
    print("If your guess is within 10 of my number, I'll tell you that you are WARM.")
    print(
        "If your guess is farther than your most recent guess, I'll say you're getting COLDER."
    )
    print(
        "If your guess is closer than your most recent guess, I'll say you're getting WARMER."
    )
    print("Erroneous guesses are not counted.")
    print("LET'S PLAY!\n")


def is_out_of_bounds(num):
    return (num < 1) or (num > 100)


def check_entered_guess():
    while True:
        try:
            entered_guess = int(input("Guess the number between 1 and 100: "))

            if is_out_of_bounds(entered_guess):
                raise OutOfBoundsError

            return entered_guess

        except ValueError:
            print("The given input is not a natural number.\n")

        except OutOfBoundsError:
            print("OUT OF BOUNDS\n")


def is_first_turn(turn):
    return turn == 1


def is_guess_close(guessed_num):
    return abs(guessed_num - selected_num) <= 10


def is_current_guess_closer_than_prev_guess(current_guess, prev_guess):
    return abs(current_guess - selected_num) < abs(prev_guess - selected_num)


def guessing(num_guesses=0, prev_guess=None):
    global selected_num

    selected_num = random.randint(1, 100)
    print(selected_num)

    while True:
        entered_guess = check_entered_guess()
        num_guesses += 1

        if entered_guess == selected_num:
            return num_guesses

        if is_first_turn(num_guesses) and is_guess_close(entered_guess):
            print("WARM!\n")
        elif is_first_turn(num_guesses):
            print("COLD!\n")
        elif is_current_guess_closer_than_prev_guess(entered_guess, prev_guess):
            print("WARMER!\n")
        else:
            print("COLDER!\n")

        prev_guess = entered_guess


def check_continue_respone():
    while True:
        user_input = input("\nDo you want to continue playing? (Y/N): ")

        if user_input.upper() in ["Y", "N"]:
            return user_input.upper()

        print(f"Sorry '{user_input}' is not a valid command.\n")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
