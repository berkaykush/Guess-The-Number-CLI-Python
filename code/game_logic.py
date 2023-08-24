import math
import os
import random
import textwrap

from out_of_bounds_error import OutOfBoundsError


class GameLogic:
    LOWER_BOUND = 1
    UPPER_BOUND = 100
    CLOSE_GUESS_THRESHOLD = 10

    def __init__(self):
        self.__num_guesses = 0
        self.__num_chances = round(math.log(self.UPPER_BOUND - self.LOWER_BOUND + 1, 2))
        self.__selected_num = self.__pick_random_num()

    @property
    def num_guesses(self):
        return self.__num_guesses

    def __pick_random_num(self):
        return random.randint(self.LOWER_BOUND, self.UPPER_BOUND)

    def run(self):
        self.__clear_terminal()
        self.__print_welcome_message()
        prev_guess = None

        while True:
            entered_guess = self.__check_entered_guess()
            self.__num_guesses += 1

            if entered_guess == self.__selected_num:
                print(
                    f"Congratulations! You guessed the number in {self.__num_guesses} guesses.\n"
                )
                return

            self.__num_chances -= 1

            if self.__num_chances == 0:
                print(
                    f"Sorry, you ran out of guesses. The number was {self.__selected_num}\n"
                )
                return

            if self.__is_first_turn(self.__num_guesses) and self.__is_guess_close(
                entered_guess
            ):
                print("WARM!\n")
            elif self.__is_first_turn(self.__num_guesses):
                print("COLD!\n")
            elif self.__is_current_guess_closer_than_prev_guess(
                entered_guess, prev_guess
            ):
                print("WARMER!\n")
            else:
                print("COLDER!\n")

            prev_guess = entered_guess

    def __clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def __print_welcome_message(self):
        print(
            textwrap.dedent(
                f"""
              WELCOME TO GUESS ME!
              I'm thinking of a number between {self.LOWER_BOUND} and {self.UPPER_BOUND}.

              If your guess is more than {self.CLOSE_GUESS_THRESHOLD} away from my number, I'll tell you you're COLD.
              If your guess is within {self.CLOSE_GUESS_THRESHOLD} of my number, I'll tell you that you are WARM.

              Also, I'll say you're getting COLDER if your guess is farther than your most recent guess,
              and WARMER if your guess is closer than your most recent guess.

              Invalid inputs are not counted as guesses and you have only {self.__num_chances} chances to guess the number.
              LET'S PLAY!
              """
            )
        )

    def __check_entered_guess(self):
        while True:
            try:
                entered_guess = int(
                    input(
                        f"Guess the number between {self.LOWER_BOUND} and {self.UPPER_BOUND}: "
                    ).strip()
                )

                if self.__is_out_of_bounds(entered_guess):
                    raise OutOfBoundsError

                return entered_guess

            except ValueError:
                print("The given input is not a natural number.\n")

            except OutOfBoundsError:
                print("The input is not in the expected range.\n")

    def __is_out_of_bounds(self, num):
        return num < self.LOWER_BOUND or num > self.UPPER_BOUND

    def __is_first_turn(self, turn):
        return turn == 1

    def __is_guess_close(self, guessed_num):
        return abs(guessed_num - self.__selected_num) <= self.CLOSE_GUESS_THRESHOLD

    def __is_current_guess_closer_than_prev_guess(self, current_guess, prev_guess):
        return abs(current_guess - self.__selected_num) < abs(
            prev_guess - self.__selected_num
        )

    @staticmethod
    def check_continue():
        while True:
            user_input = input("\nDo you want to continue playing? (Y/N): ").strip()

            if user_input.upper() in ["Y", "N"]:
                return user_input.upper()

            print(f"Sorry '{user_input}' is not a valid command.\n")

    def reset(self):
        self.__num_guesses = 0
        self.__num_chances = round(math.log(self.UPPER_BOUND - self.LOWER_BOUND + 1, 2))
        self.__selected_num = self.__pick_random_num()

    @staticmethod
    def print_goodbye_message():
        print("\nThank you for playing!\n")
