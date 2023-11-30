import random




# Return random player
def get_random_player(number_of_players):
    player  = random.randint(1, number_of_players)
    return player


# Define Player class
# TO DO
class Player:
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

