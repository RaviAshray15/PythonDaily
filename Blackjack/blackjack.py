import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Change Ace from 11 to 1 if score is above 21
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"

    elif computer_score == 0:
        return "You lose, computer has Blackjack!"

    elif user_score == 0:
        return "You win with Blackjack!"

    elif user_score > 21:
        return "You went over. You lose!"

    elif computer_score > 21:
        return "Computer went over. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"


def blackjack():

    user = [deal_card(), deal_card()]
    comp = [deal_card(), deal_card()]

    game_over = False

    while not game_over:

        user_score = calculate_score(user)
        comp_score = calculate_score(comp)

        print(f"\nYour cards: {user}")
        print(f"Your score: {user_score}")

        print(f"Computer's first card: {comp[0]}")

        # Check for Blackjack or bust
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True

        else:
            choice = input("Type 'y' to get another card, or 'n' to pass: ")

            if choice == "y":
                user.append(deal_card())

            else:
                game_over = True

    # Computer keeps drawing until score is at least 17
    while comp_score != 0 and comp_score < 17:
        comp.append(deal_card())
        comp_score = calculate_score(comp)

    print("\n--------------------")
    print(f"Your final hand: {user}")
    print(f"Your final score: {user_score}")

    print(f"Computer's final hand: {comp}")
    print(f"Computer's final score: {comp_score}")

    print("\n" + compare(user_score, comp_score))


while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()