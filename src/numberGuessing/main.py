import random

def main():
    print("Hello, Folk!")

def guess_number():

    print("Welcome to the number guessing game!")
    print("Select a Level:")
    print("1. 1 to 50 (Easy)")
    print("2. 1 to 100 (Medium)")
    print("3. 1 to 1000 (Hard)")

    level = int(input("Enter your choice: "))
    max_range = 100
    number_of_guesses = 3

    match level:
        case 1:
            print("You have selected Easy mode.")
            max_range = 50
        case 2:
            print("You have selected Medium mode.")
            max_range = 100
        case 3:
            print("You have selected Hard mode.")
            max_range = 1000
        case _:
            print("Invalid choice. Please select a valid level.")


    print("I'm thinking of a number between 1 and " + str(max_range) + ".")

    print("You have " + str(number_of_guesses) + " guesses. Good luck!")

    number = random.randint(1, max_range)

    print(number)
    while number_of_guesses > 0:
        number_of_guesses = number_of_guesses - 1

        if number_of_guesses == 0:
            print("This is your last guess.")

        guess = int(input("Make a guess: "))

        if guess == number:
            print("Congratulations! You guessed the number " + str(guess) + ".")
            break

        if guess > number:
            print("Your guess " + str(guess) + " is too high. Try again.")
        elif guess < number:
            print("Your guess " + str(guess) + " is too low. Try again.")

        if number_of_guesses == 0:
            print("Sorry, you've run out of guesses. The number was " + str(number) + ". /<br> Better luck next time!")
            break;



if __name__ == "__main__":
    main()
    guess_number()
