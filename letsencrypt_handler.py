"""Basic wsgi handler for letsencrypt challenge/response pairs"""

import webapp2

CHALLENGE_RESPONSES = {
}


class LetsEncryptHandler(webapp2.RequestHandler):
    """Simple letsencrypt challenge/response handler."""

    def get(self, challenge):
        """Given a challenge, get a response."""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(CHALLENGE_RESPONSES.get(challenge, ''))

app = webapp2.WSGIApplication([
    (r'/.well-known/acme-challenge/([\w-]+)', LetsEncryptHandler),
])
