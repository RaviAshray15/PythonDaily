
import random

from hangman_words import word_list


# ==========================================
# GAME SETTINGS
# ==========================================

lives = 6
game_over = False

correct_letters = []


# ==========================================
# CHOOSE A RANDOM WORD
# ==========================================

chosen_word = random.choice(word_list)


# ==========================================
# CREATE PLACEHOLDER
# ==========================================

placeholder = ""

for char in chosen_word:
    placeholder += "_ "

print(placeholder)


# ==========================================
# GAME LOOP
# ==========================================

while not game_over:

    print(f"\n*********************** {lives}/6 LIVES LEFT!! ***********************")

    guess = input("\nGuess a letter: ").lower()


    # ======================================
    # CHECK THE GUESSED LETTER
    # ======================================

    display = ""

    for char in chosen_word:

        if char == guess:
            display += char

            if guess not in correct_letters:
                correct_letters.append(guess)

        elif char in correct_letters:
            display += char

        else:
            display += "_"


    # ======================================
    # DISPLAY CURRENT WORD
    # ======================================

    print(display)


    # ======================================
    # CHECK FOR WRONG GUESS
    # ======================================

    if guess not in display:

        lives -= 1

        if lives == 0:
            game_over = True
            print("\nYou lose!")
            print("Correct word is:", chosen_word)

        else:
            print("Wrong guess!")


    # ======================================
    # CHECK FOR WIN
    # ======================================

    if "_" not in display:

        game_over = True
        print("\nYou win!")