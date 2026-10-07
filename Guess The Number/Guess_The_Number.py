import random
from art import logo, won, lose, easy, hard

play_again = True


def easy_game(number):
    print(easy)
    attempts = 10

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high!!")
            attempts -= 1

        elif guess < number:
            print("Too low!!")
            attempts -= 1

        else:
            print(won)
            print("YOU GUESSED IT RIGHT!!")
            break

    if attempts == 0:
        print(lose)
        print(f"\nYou ran out of attempts! The number was {number}.")


def hard_game(number):
    print(hard)
    attempts = 5

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high!!")
            attempts -= 1

        elif guess < number:
            print("Too low!!")
            attempts -= 1

        else:
            print(won)
            print("YOU GUESSED IT RIGHT!!")
            break

    if attempts == 0:
        print(lose)
        print(f"\nYou ran out of attempts! The number was {number}.")


def game():
    global play_again

    print(logo)
    print("\nWelcome to the Number Guessing Game!")

    while play_again:

        number = random.randint(1, 100)
    
        print("\nI am thinking of a number between 1 and 100")

        difficulty = input(
            "\nChoose a difficulty. Type 'easy' or 'hard': "
        )

        if difficulty.lower() == "easy":
            easy_game(number)

        elif difficulty.lower() == "hard":
            hard_game(number)

        else:
            print("Enter a valid option!!!")
            continue

        again = input(
            "\nType 'y' to try again with a different number. "
            "Type 'n' to stop: "
        )

        if again.lower() == "n":
            play_again = False

    print("\nThanks for playing!!!")


game()