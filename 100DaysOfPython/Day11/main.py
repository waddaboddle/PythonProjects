import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_check(cards_in_hand):
    if cards_in_hand.count(11) > 0:
        cards_in_hand[cards.index(11)] = 1


def continue_check(player_cards, player_total, dealer_cards, dealer_total):
    """Checks if the total is less, greater or equal to 21"""
    if player_total == 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Player wins! ")
        return False
    elif player_total > 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Dealer wins! ")
        return False
    else:
        return True


def win_check(player_cards, player_total, dealer_cards, dealer_total):
    if player_total == 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Player wins! ")
        return False
    elif player_total > 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Dealer wins! ")
        return False
    elif dealer_total == 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Dealer wins!")
        return False
    elif dealer_total > 21:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Player wins!")
        return False
    elif player_total > dealer_total:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Player wins!")
        return False
    elif dealer_total > player_total:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Dealer wins!")
        return False
    elif dealer_total == player_total:
        print(f"    Your final hand {player_cards}, final score: {player_total} ")
        print(f"    Dealers final hand: {dealer_cards}, final score: {dealer_total}")
        print("Draw!")
        return False
    else:
        return True


def blackjack():
    global hit
    start = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    player_cards = [random.choice(cards), random.choice(cards)]
    # player_cards = [11, 10]
    player_total = sum(player_cards)
    if player_total > 21:
        ace_check(player_cards)

    dealer_cards = [random.choice(cards), random.choice(cards)]
    dealer_total = sum(dealer_cards)
    while dealer_total < 17:
        dealer_cards.append(random.choice(cards))
        dealer_total = sum(dealer_cards)
        if dealer_total > 21:
            ace_check(dealer_cards)

    if start == "y":
        game_start = True
        print(art.logo)
    else:
        print("Bye!")
        game_start = False

    while game_start:
        player_total = sum(player_cards)
        dealer_total = sum(dealer_cards)

        print(f"    Your cards: {player_cards}, current score: {player_total}")
        print(f"    Dealers first card: {dealer_cards[0]}")

        game_start = continue_check(player_cards, player_total, dealer_cards, dealer_total)
        if not game_start:
            hit = "n"
            blackjack()
        if game_start:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")

        while hit == "y":
            player_cards.append(random.choice(cards))
            player_total = sum(player_cards)
            if player_total > 21:
                ace_check(player_cards)
            print(f"    Your cards: {player_cards}, final score: {player_total}")
            print(f"    Dealers first card: {dealer_cards[0]}")
            game_start = continue_check(player_cards, player_total, dealer_cards, dealer_total)
            if not game_start:
                hit = "n"
                blackjack()
            if game_start:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            if game_start:
                game_start = win_check(player_cards, player_total, dealer_cards, dealer_total)
                blackjack()


blackjack()
