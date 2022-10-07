#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)
_.__doc__ = "gettext documentation"


class Config(object):
    """ Configure class is passed in object which is a
        default value in pythonthat isnherits from the base class
        but possess no attributes and cant be given any
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
_('home_title')
_('home_header')


@babel.localeselector
def get_locale():
    """ get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
