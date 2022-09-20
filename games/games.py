import guessing
import hangmann


def jogar():
    print("Choose your game:")
    print("(1) hangman - (2) guessing")

    game = int(input("Choose your game:"))

    if game == 1:
        hangmann.play_hangman()
    elif game == 2:
        guessing.play_guessing()


if __name__ == "__main__":
    jogar()


    