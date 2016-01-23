"""Routes for gwax_flask."""

from gwax_flask import app
from gwax_flask import handlers
from gwax_flask import views


for error_code in range(400, 420) + range(500, 506):
    app.error_handler_spec[None][error_code] = handlers.error_handler


app.add_url_rule('/dynamictest', 'index', view_func=views.index)
