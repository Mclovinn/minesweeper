#!/usr/bin/env python3
# define simple flask app
from flask import Flask,render_template
from model.models import MineSweeper

app = Flask(__name__)

minesweeper = MineSweeper()


@app.route('/')
def hello_world():
    return render_template('index.html', minetable=minesweeper.minestable)


if __name__ == "__main__":
    app.run()
