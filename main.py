from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cloned_list = cards


def pick_random_card():
    random_card = random.choice(cloned_list)
    cloned_list.remove(random_card)
    return random_card


def calculate_score(cards_list):
    # Hand with blackjack (10 + 11)
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0

    # Check if 11 needs to be change to 1
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(pick_random_card())
        computer_cards.append(pick_random_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User cards {user_cards} and sum is {sum(user_cards)}")
        print(f"Computer first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card or type 'n' to pass: ")
            if choice == "y":
                user_cards.append(pick_random_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(pick_random_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, final score {user_score}")
    print(f"Opponent finad hand is {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
