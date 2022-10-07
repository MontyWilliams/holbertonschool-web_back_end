#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)
_.__doc__ = "gettext documentation"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index page
    """
    return render_template('5-index.html')


@app.before_request
def before_request():
    """ stores user to global var
    """
    user = get_user()
    if user:
        g.user = user


def get_user():
    """ returns an int representing the user id
    """
    try:
        user_id = int(request.args.get('login_as'))
    except Exception:
        return None
    return users.get(user_id)

if __name__ == '__main__':
    app.run(debug=True)
