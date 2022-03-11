class Game:
    def __init__(self, players):
        self.players = players
    
    def game_result(self):
        player_1 = self.players[0]
        player_2 = self.players[1]
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
