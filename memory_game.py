import random
import cards
import interface
import players
import play


# Higher or lower memory game
def main():
    
    rules = "For every card in your hand, starting with the first and ending with the last, you will be shown another random card. \
You have to remember if your card was higher or lower. If you are right, you score one point. \
If you are wrong, if both cards are the same, or if either card is a joker, you lose one point."

    # Print any opening text etc.
    play_opening()
    # Get number of players and randomly pick starting player
    max_players = 10
    players_total = interface.get_players(max_players) # int
    first_player = players.get_random_player(players_total) # int, 1-indexed
    # Make list of players
    player_list = players.make_players(players_total, first_player)
    # Get number of jokers to put in deck
    max_jokers = 4
    jokers = cards.get_jokers(max_jokers)
    # Build deck
    deck = cards.build_deck(jokers)
    # Optionally shuffle and print deck until user is ready
    while True:
        cards.ask_shuffle(deck)
        cards.ask_print_deck(deck)
        if interface.ask_ready_to_continue():
            break
    # Deal hands to players
    hands = cards.deal_hands(deck, players_total)
    # Build new shuffled deck
    deck = cards.build_deck(jokers)
    random.shuffle(deck)
    # Print line to indicate next phase
    interface.new_phase()
    # Print the first player's hand
    for player_index in range(players_total):
        current_player = player_list[player_index]
        # Prints player number and their hand
        print(f"Current player: {current_player}")
        print(f"{current_player}'s hand:")
        current_hand = cards.get_hand(hands, player_index)
        cards.print_hand(current_hand)
        # Number of cards in player's hand
        cards_total = len(current_hand)
        print(f"Number of cards in hand: {cards_total}")
        # Print line to indicate next phase
        interface.new_phase()
        # Print rules
        print(rules)
        interface.new_phase()
        play.round(current_player, current_hand, deck)


# Print opening text
def play_opening():
    print("Welcome to the card hand-dealing game!")


if __name__ == "__main__":
    main()
