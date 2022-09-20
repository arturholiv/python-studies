import guessing
import hangmann


print("Choose your game:")
print("(1) hangman - (2) guessing")

game = int(input("Choose your game:"))

if game == 1:
    hangmann.play_hangman()
elif game == 2:
    guessing.play_guessing()
    