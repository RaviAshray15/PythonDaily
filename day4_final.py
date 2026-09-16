
list = ['rock', 'paper', 'scissors']

import random

user = int(input("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissors\nEnter your input: "))
computer = random.randint(0, 2)

if user > 2 or user < 0:
    print("Enter a valid number!!!")
    exit()

print(f"\nYou chose: {list[user]}")
print(f"Computer chose: {list[computer]}")


if user == 0 and computer == 2:
    print("You win!")

elif computer == 0 and user == 2:
    print("You lose!")
    
elif computer > user:
    print("You lose!")
    
elif user == computer:
    print("It's a draw!")
