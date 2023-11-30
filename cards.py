import random

# ace value = 14
# Ace positions: -1 = aces low, 1 = aces high, 0 = aces loop from "K" to "2"
# e.g.: ace_position = 0
   
# Optionally print every card in deck
def ask_print_deck(deck):
    while True:
        answer = input("Show cards in deck? y/n\n").strip().lower()
        if answer == "y":
            for card in deck:
                print(f"{card}")
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid response")


# Optionally shuffle deck
def ask_shuffle(deck):
    while True:
        answer = input("Shuffle deck? y/n\n").strip().lower()
        if answer == "y":
            random.shuffle(deck)
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid response")


# Build standard 52-card deck plus given number of jokers
def build_deck(jokers):
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for number in numbers:
        for suit in suits:
            card = Card(number, suit)
            deck.append(card)
    for i in range(jokers):
        deck.append(Card(i + 1, "Jokers"))
    return deck


# Returns True if cards are adjacent else False
# Returns False is either card is a Joker
def adjacent(card1, card2, ace_position):
    return values_within_range(card1, card2, 1, ace_position)
    

# Sees if two cards are within a given range and returns True or False
# Returns False if either card is a Joker
# Returns False if raises error
def values_within_range(card1, card2, range, ace_position):
    try:
        if card1.suit == "Jokers" or card2.suit == "Jokers":
            return False
        # Assign value to int
        c1 = card1.value
        c2 = card2.value
        # If aces cyclic
        if ace_position == 0:
            # Check for 3 differences: without looping, looping up from c1, and looping up from c2
            differences = [
                abs(c1 - c2), 
                abs((c1 + 13) - c2), 
                abs(c1 - (c2 + 13))
                ]
            # Pick smallest difference
            difference = min(differences)
        # If aces high or low
        elif ace_position in [-1, 1]:
            # If aces low, set ace values to 1
            if ace_position == -1:
                if c1 == 14:
                    c1 = 1
                if c2 == 14:
                    c2 = 1
            # Difference between card values
            difference = abs(c1 - c2)
        # Return True if within range, else False
        if difference <= range:
            return True
        else:
            return False
    except:
        return False


# Deal the whole deck to all players, one card at a time, starting with player one
def deal_hands(deck, players_total):
    min = 0
    max = players_total - 1
    current = 0
    hands = []
    for _ in range(players_total):
        hands.append([])
    while len(deck):
        hands[current].append(deck.pop(0))
        current += 1
        if current > max:
            current = 0
    return hands


# Return hand for given player
def get_hand(hands, player):
    return hands[player-1]


# Prompt user for number of jokers until valid answer given, returning number
def get_jokers(max):
    if max == 0:
        return 0
    while True:
        try:
            jokers = int(input("Number of jokers: "))
            if jokers not in range(0, max + 1):
                print(f"Must be a number between 0 and {max}")
                continue
            return jokers
        except:
            print("Must be a number")
            continue


# Return Card
def make_card(number, suit):
    return Card(number, suit)


# Print every card in a hand
def print_hand(hand):
    for card in hand:
        print(f"{card}")


# Take a card and return the value above it or None
def value_above(card, ace_position):
    if card.suit == "Jokers":
        above = None
    elif card.value == 1:
        above = 2
    elif card.value == 13:
        if ace_position in [0, 1]:
            above = 14
        else:
            above = None
    elif card.value == 14:
        if ace_position in [0, -1]:
            above = 2
        else:
            above = None
    elif card.value in range(2, 13):
        above = card.value + 1
    else:
        above = None
    return above


# Take a card and return the value below it or None
def value_below(card, ace_position):
    if card.suit == "Jokers":
        below = None
    elif card.value == 2:
        if ace_position in [0, -1]:
            below = 14
        elif ace_position == 1:
            below = None
        else:
            below = None
    elif card.value == 14:
        if ace_position in [0, 1]:
            below = 13
        else:
            below = None
    elif card.value in range(3, 14):
        below = card.value - 1
    else:
        below = None
    return below


# Define Card class
class Card:
    # Joker syntax: name is "Joker", suit is "Jokers", number is string starting at "1", color is "Jokers"
    """
    self.suit
    self.number
    self.name
    self.value
    self.color
    """
    # __init__ always called when creating object
    # definte to initialize the contents of an object from this class
    # self gives access to the current object that was just created
    def __init__(self, number, suit):
        # Suit is set before number as Joker is a special case
        # Validate suit
        if suit not in ["Hearts", "Diamonds", "Clubs", "Spades", "Jokers"]:
            raise ValueError("Invalid suit when making card")
        # Set suit
        try:
            self.suit = suit
        except:
            raise ValueError("Error setting suit")
        # Validate number for non-joker cards
        if suit != "Jokers":
            if number not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                raise ValueError("Invalid number when making card")
        # Validate number for joker cards
        else:
            try:
                if int(number) not in range(1, 5):
                    raise ValueError("Number outside valid range when making joker card")
            except:
                raise ValueError("Invalid number when making joker card")
        # Set number
        try:
            self.number = number
        except:
            raise ValueError("Error setting number")
        # Set name
        try:
            if suit == "Jokers":
                self.name = "Joker"
            else:
                self.name = f"{self.number} of {self.suit}"
        except:
            raise ValueError("Error setting name")
        # Set value
        try:
            if suit != "Jokers":
                if self.number == "Jack":
                    self.value = 11
                elif self.number == "Queen":
                    self.value = 12
                elif self.number == "King":
                    self.value = 13
                elif self.number == "Ace":
                    self.value = 14
                else:
                    self.value = int(self.number)
            else:
                self.value = int(self.number)
        except:
            raise ValueError("Error setting value")
        # Set color
        try:
            if self.suit in ["Hearts", "Diamonds"]:
                self.color = "Red"
            elif self.suit in ["Clubs", "Spades"]:
                self.color = "Black"
            elif self.suit == "Jokers":
                self.color = "Jokers"
            else:
                raise ValueError("Error setting color, check suits")
        except:
            raise ValueError("Error setting color")

    # Use user-friendly self.name for visible strings
    def __str__(self):
        return self.name

    # Getters - always one argument
    @property
    def number(self):
        return self._number

    @property
    def suit(self):
        return self._suit

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def color(self):
        return self._color

   # Setters - always two arguments
    @number.setter
    def number(self, number):
        self._number = number

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    @name.setter
    def name(self, name):
        self._name = name

    @value.setter
    def value(self, value):
        self._value = value

    @color.setter
    def color(self, color):
        self._color = color

