from flask import render_template
from app import app
from models.player_list import players
from models.game_list import game

@app.route('/home')
def index():
    return render_template('index.html', title="Home")

@app.route('/play')
def play():
    return render_template('play.html', title="Play Game")

@app.route('/<p1_choice>/<p2_choice>')
def result(p1_choice, p2_choice):
    players[0].choice = p1_choice
    players[1].choice = p2_choice
    winner = game.game_result()
    return render_template('game_result.html', title='Game Result', player_1=players[0], player_2=players[1], winner=winner)
