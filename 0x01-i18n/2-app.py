#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configure class is passed in object which is a
        default value in pythonthat isnherits from the base class
        but possess no attributes and cant be given any
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def index():
    """ index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
