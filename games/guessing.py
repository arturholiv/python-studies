print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 33
total_attempts = 3
round_is = 1


while round_is <= total_attempts:
    answer_str = input("Type your number: ")

    answer_int = int(answer_str)
    print("You typed: ", answer_str)

    got_it_right = answer_int == secret_number
    higher = answer_int > secret_number
    lowest = answer_int < secret_number

    print("Attempt ", round_is, "of ", total_attempts)
    if got_it_right:
        print("You're right")
    else:
        if higher:
            print("You're wrong! :/ Your attempt was higher than the number ")
        elif lowest:
            print("You're wrong! :/ Your attempt was lower than the number ")
    round_is = round_is + 1
