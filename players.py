import random
import statistics

# Return random player
def get_random_player(number_of_players):
    player  = random.randint(1, number_of_players)
    return player


# Define Player class
class Player:
    # __init__ always called when creating object
    # definte to initialize the contents of an object from this class
    # self gives access to the current object that was just created
    def __init__(self, name):
        # Set name
        try:
            self.name = name
        except:
            raise ValueError
        # Set empty list of scores
        self.scores = []
        
    # Use name for strings
    def __str__(self):
        return self.name
    
    def add_score(self, score):
        try:
            self.scores.append(float(score))
        except:
            raise ValueError
        

    def reset_scores(self):
        self.scores = []

    # Getters - always one argument
    @property
    def name(self):
        return self._name
    
    @property
    def scores(self):
        return self._scores
    
    # Most recent score
    @property
    def score(self):
        if len(self.scores)== 0:
            return None
        return self._scores[-1]

    @property
    def high_score(self):
        if len(self.scores)== 0:
            return None
        return max(self._scores)

    @property
    def low_score(self):
        if len(self.scores)== 0:
            return None
        return min(self._scores)

    @property
    def average_score(self):
        if len(self.scores)== 0:
            return None
        return statistics.fmean(self._value)
    
    # Number of scores in scores list
    @property
    def games_played(self):
        return len(self._scores)

   # Setters - always two arguments
    @name.setter
    def name(self, name):
        self._name = f"{name}"

    @scores.setter
    def scores(self, scores):
        self._scores = scores