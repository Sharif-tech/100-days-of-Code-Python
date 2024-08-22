import random
import sys
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# deal cards
def deal_card(get_cards):
    """Returns a random card from the deck."""
    return random.choice(get_cards)


# summing cards
def calculate_score(score):
    # check for blackjack
    if len(score) == 2 and sum(score) == 21:
        return 0

    # check for ace
    if 11 in score and sum(score) > 21:
        score.remove(11)
        score.append(1)

    return sum(score)


# compare scores
def compare(u_score, comp_score):
    if u_score == comp_score:
        print("It is a draw!")
    elif comp_score == 0:
        print("You lose! \U0001F622 computer has a Blackjack")
    elif u_score == 0:
        print("You win! \U0001F604 with a Blackjack")
    elif u_score > 21:
        print("You lose! \U0001F622 You went over")
    elif comp_score > 21:
        print("Computer lose! It went over")
    else:
        if u_score > comp_score:
            print("You win! \U0001F604")
        else:
            print("Computer win!")

    blackjack()


def blackjack():
    # draw_card = True
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

        # print logo
        print(logo)

        # Deal the user and computer 2 cards each using deal_card() and append().
        user_cards = []
        computer_cards = []

        for _ in range(2):
            user_cards.append(deal_card(cards))
            computer_cards.append(deal_card(cards))

        print(f"Your cards: {user_cards} current score: {calculate_score(user_cards)}, "
              f"Computer's first card: {computer_cards[0]}")

        draw_card = True
        while draw_card:
            if ((calculate_score(user_cards) == 0) or (calculate_score(computer_cards) == 0)) or \
                    ((calculate_score(user_cards)) > 21):
                # game over
                print(f"Your final hand: {user_cards} final score: {calculate_score(user_cards)}, "
                      f"Computer's final hand: {computer_cards} final score: {calculate_score(computer_cards)}")
                compare(calculate_score(user_cards), calculate_score(computer_cards))
                draw_card = False

                print(f"Your cards: {user_cards} current score: {calculate_score(user_cards)}, "
                      f"Computer's first card: {computer_cards[0]}")

            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == "y":
                user_cards.append(deal_card(cards))
                calculate_score(user_cards)
                print(f"Your cards: {user_cards} current score: {calculate_score(user_cards)}, "
                      f"Computer's first card: {computer_cards[0]}")
            else:
                computer_cards.append(deal_card(cards))
                calculate_score(computer_cards)
                if sum(computer_cards) > 17:
                    draw_card = False

                print(f"Your final hand: {user_cards} final score: {calculate_score(user_cards)}, "
                      f"Computer's final hand: {computer_cards} final score: {calculate_score(computer_cards)}")
                compare((calculate_score(user_cards)), (calculate_score(computer_cards)))

        # start again
        blackjack()
    else:
        # exit app
        sys.exit()


# start again
blackjack()
