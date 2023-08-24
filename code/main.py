from game_logic import GameLogic


def main():
    game = GameLogic()

    while True:
        game.run()

        if game.check_continue() == "N":
            break

        game.reset()

    game.print_goodbye_message()


if __name__ == "__main__":
    main()
