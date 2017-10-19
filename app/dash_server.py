import tornado.ioloop
import tornado.web
from .settings import SETTINGS, APP_PATH
from .routes import ROUTES
import sys
from tornado.options import options, define
from os.path import join, dirname
import logging

logging.basicConfig(filename=join(dirname(APP_PATH), 'logs', 'server.log'), level=logging.INFO)

define('port', 8888)


def make_app():
    return tornado.web.Application(
        ROUTES,
        **SETTINGS
    )


if __name__ == "__main__":
    args = sys.argv
    options.parse_command_line(args)

    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()