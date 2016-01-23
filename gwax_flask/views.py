"""View functions for gwax_flask."""

from flask.ext.mako import render_template


def index():
    return render_template('base.mako', data='value thing')
