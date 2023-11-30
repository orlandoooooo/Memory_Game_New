import random
import cards
import interface
import players


# Higher or lower memory game
def main():
    
    rules = "For every card in your hand, starting with the first and ending with the last, you will be shown another random card. \
        You have to remember if your card was higher or lower.\nIf you are right, you score one point. \
            If you are wrong, if both cards are the same, or if either card is a joker, you lose one point."

    # Print any opening text etc.
    play_opening()
    # Get max players and randomly pick starting player
    max_players = 10
    players_total = interface.get_players(max_players)
    current_player = players.get_random_player(players_total)
    # Get numbre of jokers to put in deck
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
    # Print line to indicate next phase
    interface.new_phase()
    # Print the first player's hand
    print(f"Randomly selected first player.\nCurrent player: Player {current_player}")
    print(f"Player {current_player}'s hand:")
    current_hand = cards.get_hand(hands, current_player)
    cards.print_hand(current_hand)
    # Number of cards in player's hand
    cards_total = len(current_hand)
    print(f"Number of cards in hand: {cards_total}")
    # Game starts for current player only
    """
    For every card in their hand starting with the first, they are shown a card from a new, shuffled deck
    They have to remember if their card was higher or lower than the random card
    If they are right, they gain a point
    If they are wrong, the cards match, or either card is a joker, they lose a point
    """
    # Print line to indicate next phase
    interface.new_phase()
    # Print rules
    print(rules)
    interface.new_phase()
    # Build shuffled deck
    deck = cards.build_deck(jokers)
    random.shuffle(deck)
    # Set starting score
    score = 0
    # Set aces as high
    ace_position = 1
    # Wait till user is ready
    print(f"Player {current_player}, get ready to play.")
    while True:
        if interface.ask_ready_to_continue():
            break
    # Print lines to hide player's hand
    interface.clear_screen()
    # For every card in hand
    for i in range(cards_total):
        # Show card from new deck
        new_card = deck[i]
        player_card = current_hand[i]
        print(f"Card {i}:\n{new_card}")
        # Lose one point if either card is a joker
        if player_card.suit == "Jokers" or new_card.suit == "Jokers":
            # Lose one point for joker
            print("JOKER! 1 point deducted.")
            score -=1
        else:
            # Ask higher or lower. Any other answer loses a point
            answer = input("Choose higher or lower? h/l ").strip().lower()
            if answer == "h":
                # If player card is higher than new card, gain one point, else lose one point
                if player_card.value == new_card.value:
                    print("Cards matched. 1 point deducted.")
                    score -= 1
                elif cards.value_above(new_card, ace_position) == None:
                    print("Incorrect. 1 point deducted.")
                    score -= 1
                elif player_card.value >= cards.value_above(new_card, ace_position):
                    print("Correct! You score 1 point.")
                    score += 1
                else:
                    print("Incorrect. 1 point deducted.")
                    score -= 1
            elif answer == "l":
                # If player card is higher than new card, gain one point, else lose one point
                if player_card.value == new_card.value:
                    print("Cards matched. 1 point deducted.")
                    score -= 1
                elif cards.value_below(new_card, ace_position) == None:
                    print("Incorrect. 1 point deducted.")
                    score -= 1
                elif player_card.value <= cards.value_below(new_card, ace_position):
                    print("Correct! You score 1 point.")
                    score += 1
                else:
                    print("Incorrect. 1 point deducted.")
                    score -= 1
            else:
                # Lose one point for invalid response
                print("Invalid answer. 1 point deducted.")
                score -= 1
    print(f"Final score: {score}")


# Print opening text
def play_opening():
    print("Welcome to the card hand-dealing game!")


if __name__ == "__main__":
    main()
