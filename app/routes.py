import tornado.web
from app.handlers.main import MainHandler
from app.handlers.dashboard import DashboardHandler
from .settings import SETTINGS


ROUTES = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": SETTINGS['static_path']}),
    (r"/dashboard", DashboardHandler),
    (r"/", MainHandler),
]