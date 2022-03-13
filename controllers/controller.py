from flask import render_template, request
from app import app
from models.player import Player, player_1, player_2
from models.game import Game

@app.route('/home')
def index():
    return render_template('index.html', title='Home')

@app.route('/play')
def play():
    return render_template('play.html', title='Play Game')

@app.route('/<p1_choice>/<p2_choice>')
def result(p1_choice, p2_choice):
    player_1.choice = p1_choice
    player_2.choice = p2_choice
    winner = Game.game_result(player_1, player_2)
    return render_template('game_result.html', title='Game Result', player_1=player_1, player_2=player_2, winner=winner)

@app.route('/result', methods=['POST'])
def play_game():
    player_1 = Player(request.form['name'], request.form['choice'])
    player_2 = Game.computer()
    winner = Game.game_result(player_1, player_2)
    return render_template('game_result.html', title='Game Result', player_1=player_1, player_2=player_2, winner=winner)
