import cards
import sys
import random

def main():
    ace_position = -1
    play_opening()
    max_players = 10
    players = 10
    current_player = 1
    max_jokers = 4
    jokers = 2
    deck = cards.build_deck(jokers)
    cards.ask_shuffle(deck)
    hands = cards.deal_hands(deck, players)
    print(f"Player {current_player}'s hand:")
    cards.print_hand(hands[current_player - 1])
    acespades = cards.Card("Ace", "Spades")
    print(acespades.value)
    print(cards.below(acespades, ace_position))

def ask_ready_to_continue():
    while True:
        answer = input("Ready to continue? y/n\n").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid response")    

def play_opening():
    print("Welcome to the card hand-dealing game!")

def new_phase():
    print("----------")

def get_starting_player(number_of_players):
    player  = random.randint(1, number_of_players)
    return player

def get_players(max):
    if max == 0:
        return 0
    if max == 1:
        return 1
    while True:
        try:
            players = int(input("Number of players: "))
            if players not in range(1, max + 1):
                print(f"Must be a number between 1 and {max}")
                continue
            return players
        except:
            print("Must be a number")
            continue

def make_card(number, suit):
    return None

if __name__ == "__main__":
    main()