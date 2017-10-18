def main():
    print("I'm thinking of a number between 1 and 100, can you guess it?")
    magic_number = 44
    guess = 0
    attempts = 0

    while guess != magic_number:
        guess = eval(input("What is your guess? "))
        attempts = attempts + 1

        if guess < magic_number:
            print("You're to low!")
        elif guess > magic_number:
            print("You're to high")
        else:

            print("You got it! It took you", attempts, "tries.")
main()
