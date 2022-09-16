print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 33

answer_str = input("Type your number: ")

answer_int = int(answer_str)

print("You typed: ", answer_str)

if answer_int == secret_number:
    print("You're right")
else:
    print("You're wrong! :/ The right answer was ", secret_number)
