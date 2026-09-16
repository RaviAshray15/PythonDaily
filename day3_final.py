print("Welcome to treasure island!")
print("Your mission is to find the treasure!")
first = input("You are at a cross road. Where do you want to go?\n Type 'left' or 'right': ")

if first == 'right':
    print("You fell into a hole. Game Over")
elif first == 'left':
    second = input("\nYou've come to a lake. There is an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across.\nEnter your input here: ")


if second == 'swim':
    print("You get attacked by an angry trout. Game Over.")
elif second == 'wait':
    third = input("\nYou arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\nEnter your input here: ")
    
if third == 'red':
    print("It's a room full of fire. Game Over.")
elif third == 'blue':
    print("It's a room full of beasts. Game Over.")
elif third == 'yellow':
    print('\nYou found the treasure. You win!')