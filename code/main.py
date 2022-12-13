from game_logic import (
    guessing,
    check_continue_respone,
    clear_terminal,
    print_welcome_message,
)


def main():
    running = True

    while running:
        print_welcome_message()
        print(f"\nCONGRATULATIONS, YOU GUESSED IT IN ONLY " f"{guessing()} GUESSES!!!")

        if check_continue_respone() == "N":
            running = False
            continue

        clear_terminal()


if __name__ == "__main__":
    clear_terminal()
    main()
    print("\nGOODBYE")
