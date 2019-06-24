"""
Use tornado
for high IO
for high latency
low cpu
"""

import  time
import math

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("IN GET ASIO")
        print(math.factorial(234))
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8080)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()
