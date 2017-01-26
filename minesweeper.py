#!/usr/bin/env python3
# define simple flask app
from flask import Flask,render_template, request
from model.models import MineSweeper

app = Flask(__name__)

minesweeper = MineSweeper()


@app.route('/')
def hello_world():
    return render_template('index.html', minetable=minesweeper.get_board())

@app.route('/play', methods=['POST'])
def verify_position():

    position_split = request.form['position'].split('_')
    position = (int(position_split[1]),int(position_split[2]))

    board = minesweeper.validate_position(position)
    return render_template('index.html', minetable=minesweeper.minestable, message=board[position])



if __name__ == "__main__":
    app.run()
