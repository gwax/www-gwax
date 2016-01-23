"""Flask application config for gwax_flask."""

import os
try:
    from gwax_flask.secrets import SECRET_KEY
except ImportError:
    pass

DEBUG = False
# Auto-set debug mode based on App Engine dev environ
if os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'):
    DEBUG = True

TESTING = False
