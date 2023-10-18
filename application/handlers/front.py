from flask import Blueprint, render_template

front_handler = Blueprint('front_handler', __name__)


@front_handler.route('/')
def index():
    return render_template('index.html', active='index')
