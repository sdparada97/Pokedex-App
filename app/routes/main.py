import logging

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def poke_app():
    logging.debug("debug log")
    return render_template('pokedex.html')