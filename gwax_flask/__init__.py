from flask import Flask
from flask.ext.mako import MakoTemplates

import gwax_flask.config

app = Flask(__name__)
app.config.from_object(gwax_flask.config)
mako = MakoTemplates(app)

import gwax_flask.routes
