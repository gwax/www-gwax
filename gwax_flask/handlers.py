"""Error handler."""

from flask import request
from flask.ext.mako import render_template
from mako.exceptions import TopLevelLookupException


def error_handler(error):
    """Return a custom error page."""
    code = error.code if hasattr(error, 'code') else 500
    name = error.name if hasattr(error, 'name') else 'Server error'
    if hasattr(error, 'description'):
        description = error.description
    else:
        description = 'An unknown server error has occurred.'
    view = {
        'code': code,
        'name': name,
        'description': description,
        'path': request.path,
    }
    try:
        error_page = render_template('errors/{}.mako'.format(code), **view)
    except TopLevelLookupException:
        error_page = render_template('errors/default.mako', **view)
    return error_page, code
