import tornado.web
# from handlers.main import MainHandler
# from handlers.search import MultiSearchHandler
# from handlers.proxy import UploadProxyHandler, ProxyInfoHandler
from .settings import SETTINGS


ROUTES = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": SETTINGS['static_path']}),
    # (r"/msearch", MultiSearchHandler),
    # (r"/manage/upload_proxy", UploadProxyHandler),
    # (r"/manage/proxy_info", ProxyInfoHandler),
    # (r"/", MainHandler),
]