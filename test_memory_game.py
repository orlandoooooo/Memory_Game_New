import memory_game
from cards import Card, make_card, value_above, value_below, \
    build_deck, values_within_range, adjacent
from players import Player, winning_players
import pytest

def test_make_card():
    card = make_card("Ace", "Hearts")
    assert card.color == "Red"
    assert card.value == 14
    assert f"{card}" == "Ace of Hearts"
    assert card.suit == "Hearts"
    assert card.number == "Ace"
    card = make_card("1", "Jokers")
    assert card.value == 1
    assert card.color == "Jokers"

def test_Player():
    player = Player("Player_str")
    assert f"{player}" == "Player_str"
    assert player.games_played == 0
    assert player.scores == []
    player.add_score(1)
    assert player.games_played == 1
    assert player.scores == [1]
    assert player.score == 1
    assert player.high_score == 1
    assert player.low_score == 1
    player.add_score(2)
    assert player.games_played == 2
    assert player.scores == [1, 2]
    assert player.score == 2
    assert player.high_score == 2
    assert player.low_score == 1
    player.reset_scores()
    assert player.scores == []    
    assert player.games_played == 0
    assert player.high_score == None
    assert player.low_score == None
    assert player.score == None

def test_winning_players():
    player1 = Player("Player 1")
    player1.add_score(1)
    player2 = Player("Player 2")
    player2.add_score(2)
    players = [player1, player2]
    winners = winning_players(players)
    assert len(winners) == 1
    player1.add_score(1)
    player1.add_score(2)
    winners = winning_players(players)
    assert player1.score == 2
    assert player2.score == 2
    player1.add_score(3)
    assert player1.score == 3
    assert player1.games_played == 4
    assert player2.games_played == 1
    player1.add_score(5)
    player2.add_score(5)
    winners = winning_players(players)
    assert len(winners) == 2
    player1.add_score(1)
    assert player1.score == 1
    winners = winning_players(players)
    assert len(winners) == 1
    assert winners[0].score == 5
    player1.add_score(5)
    winners = winning_players(players)
    assert len(winners) == 2
    assert winners[0].score == 5
    assert winners[1].score == 5

def test_value_above():
    card = make_card("Ace", "Diamonds")
    assert value_above(card, 0) == 2
    assert value_above(card, 1) == None
    assert value_above(card, -1) == 2
    card = make_card("Jack", "Spades")
    assert value_above(card, 0) == 12

def test_unknown_error():
    card = make_card("Ace", "Diamonds")
    card2 = make_card("Queen", "Spades")
    assert value_above(card, 1) == None
    assert value_above(card2, 1) == 13
    assert value_below(card, 1) == 13
    assert value_below(card2, 1) == 11
    assert card.value == 14
    assert card2.value == 12

    
def test_values_within_range():
    card1 = make_card("2", "Clubs")
    card2 = make_card("Ace", "Clubs")
    assert values_within_range(card1, card2, 0, -1) is False
    assert values_within_range(card1, card2, 0, 0) is False
    assert values_within_range(card1, card2, 0, 1) is False
    assert values_within_range(card1, card2, 1, -1) is True
    assert values_within_range(card1, card2, 1, 0) is True
    assert values_within_range(card1, card2, 1, 1) is False       


def test_adjacent():
    card1 = make_card("2", "Clubs")
    card2 = make_card("Ace", "Clubs")
    card3 = make_card("King", "Clubs")
    assert adjacent(card1, card2, -1) is True
    assert adjacent(card1, card2, 0) is True
    assert adjacent(card1, card2, 1) is False
    assert adjacent(card3, card2, -1) is False
    assert adjacent(card3, card2, 0) is True
    assert adjacent(card3, card2, 1) is True
    assert adjacent(card2, card1, -1) is True
    assert adjacent(card2, card1, 0) is True
    assert adjacent(card2, card1, 1) is False
    assert adjacent(card2, card3, -1) is False
    assert adjacent(card2, card3, 0) is True
    assert adjacent(card2, card3, 1) is True 
    
def test_build_deck():
    deck = build_deck(0)
    assert len(deck) == 52
    deck = build_deck(4)
    assert len(deck) == 56
    assert deck[51].value == 14
    assert deck[52].value == 1
    assert deck[52].color == "Jokers"
