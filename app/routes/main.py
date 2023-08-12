from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def poke_app():
    return render_template('pokedex.html')