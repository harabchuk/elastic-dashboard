import tornado.ioloop
import tornado.web
from ..settings import DASHBOARDS, CHARTS


class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        dashboard = DASHBOARDS[self.get_argument('name')]
        template = dashboard['template']
        for i in range(len(dashboard['charts'])):
            chart = dashboard['charts'][i]
            chart.update(CHARTS[chart['id']])
        self.render(f'dashboards/{template}', dashboard=dashboard)

