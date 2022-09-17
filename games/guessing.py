print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 33
total_attempts = 3


for round_is in range(1, total_attempts + 1):
    answer_str = input("Type a number between 1 and 15: ")

    answer_int = int(answer_str)
    print("You typed: ", answer_str)

    if answer_int < 1 or answer_int > 15:
        print("You must type a number between 1 and 15")
        print("Attempt {} of {}".format(round_is, total_attempts))
        continue

    got_it_right = answer_int == secret_number
    higher = answer_int > secret_number
    lowest = answer_int < secret_number

    print("Attempt {} of {}".format(round_is, total_attempts))
    if got_it_right:
        print("You're right")
        break
    else:
        if higher:
            print("You're wrong! :/ Your attempt was higher than the number ")
        elif lowest:
            print("You're wrong! :/ Your attempt was lower than the number ")
print("game over")
