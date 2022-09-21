import guessing
import hangmann


def play():
    print("Choose your game:")
    print("(1) hangman - (2) guessing")

    game = int(input("Choose your game:"))

    if game == 1:
        hangmann.play()
    elif game == 2:
        guessing.play()


if __name__ == "__main__":
    play()


    