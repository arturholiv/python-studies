print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 33

answer_str = input("Type your number: ")

answer_int = int(answer_str)

print("You typed: ", answer_str)

got_it_right = answer_int == secret_number
higher = answer_int > secret_number
lowest = answer_int < secret_number

if got_it_right:
    print("You're right")
else:
    if higher:
        print("You're wrong! :/ Your attempt was higher than the number ")
    elif lowest:
        print("You're wrong! :/ Your attempt was lower than the number ")
