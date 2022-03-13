import random
from models.player import Player

class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
    
    def game_result(player_1, player_2):
        player_choices = {
            "rock" : "scissors",
            "paper" : "rock",
            "scissors" : "paper"
        }
        if player_2.choice.lower() in player_choices[player_1.choice.lower()]:
            return player_1
        elif player_1.choice.lower() in player_choices[player_2.choice.lower()]:
            return player_2
        else:
            return None

    def computer():
        plays=["Rock", "Paper", "Scissors"]
        computer = Player("Computer", random.choice(plays))
        return computer
