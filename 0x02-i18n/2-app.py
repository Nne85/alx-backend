#!/usr/bin/env python3
"""
This module sets Babel’s default locale ("en") and timezone ("UTC")
using the get_locale function"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
    configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    return html
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
