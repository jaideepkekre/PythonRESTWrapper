import falcon
import sqlite3

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        """conn = sqlite3.connect('k.db')
        conn.close()"""

        resp.media = "Hello World!"

app = falcon.API()
app.add_route('/', QuoteResource())
