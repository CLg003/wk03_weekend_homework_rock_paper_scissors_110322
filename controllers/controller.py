from secrets import choice
from flask import render_template
from app import app
# from models.player import Player
# from models.player_list import players
# from models.game import Game

@app.route('/home')
def index():
    return render_template('index.html', title="Home")

# @app.route('/result/<player_1_choice>/<player_2_choice')
# def result():
#     return render_template('game_result.html', title="Game Result", player_1_choice=players[0.choice] , player_2_choice=players[1.choice])


# @app.route('/orders/<index>')
# def single_order(index):
#   chosen_order = orders[int(index)]
  
#   return render_template('order.html', order=chosen_order)