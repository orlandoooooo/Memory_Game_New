import interface
import cards
    

def round(player, hand, deck):
    # Set starting score
    score = 0
    # Set aces as high
    ace_position = 1
    # Wait till user is ready
    print(f"{player}, get ready to play.")
    while True:
        if interface.ask_ready_to_continue():
            break
    # Print lines to hide player's hand
    interface.clear_screen()
    # For every card in hand
    cards_total = len(hand)
    for i in range(cards_total):
        # Show card from new deck
        new_card = deck.pop(0)
        player_card = hand[i]
        print(f"Card {i + 1}:\n{new_card}")
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
    print(f"Final score: for {player}: {score}")
    interface.ask_ready_to_continue()