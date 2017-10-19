import tornado.web
from app.handlers.main import MainHandler
from app.handlers.dashboard import DashboardHandler
from app.handlers.chart import ChartDataHandler
from .settings import SETTINGS


ROUTES = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": SETTINGS['static_path']}),
    (r"/dashboard", DashboardHandler),
    (r"/chart_data", ChartDataHandler),
    (r"/", MainHandler),
]