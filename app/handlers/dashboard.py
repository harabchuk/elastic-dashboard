import tornado.ioloop
import tornado.web


class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        dashboard = self.get_argument('name')
        self.render(f'dashboards/{dashboard}.html',  title='Hello1')

