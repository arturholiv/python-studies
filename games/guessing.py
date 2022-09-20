import random

print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = int(random.randrange(1, 100))
total_attempts = 0
points = 1000
print("Enter the difficulty level")
print("(1) easy - (2) medium - (3) hard")

level = int(input("Choose the level: "))

if level == 1:
    total_attempts = 10
elif level == 2:
    total_attempts = 6
elif level == 3:
    total_attempts = 3

for round_is in range(1, total_attempts + 1):
    print("You have {} attempts to found the number".format(total_attempts))
    answer_str = input("Type a number between 1 and 100: ")

    answer_int = int(answer_str)
    print("You typed: ", answer_str)

    if answer_int < 1 or answer_int > 100:
        print("You must type a number between 1 and 100")
        print("Attempt {} of {}".format(round_is, total_attempts))
        continue

    got_it_right = answer_int == secret_number
    higher = answer_int > secret_number
    lowest = answer_int < secret_number

    print("Attempt {} of {}".format(round_is, total_attempts))
    if got_it_right:
        print("You're right and scored {} points".format(points))
        break
    else:
        if higher:
            print("You're wrong! Your attempt was higher than the number ")
        elif lowest:
            print("You're wrong! Your attempt was lower than the number ")
        points_lost = abs(secret_number - answer_int)
        points = points - points_lost
print("Game fished! Total points: {}, the correct answer was {}".format(points, secret_number))
