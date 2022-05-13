from flask import render_template
from . import main
from ..request import get_movies

@main.route('/')
@main.route('/home')
def index():
    movies = get_movies("popular")
    return render_template('index.html',movies=movies)