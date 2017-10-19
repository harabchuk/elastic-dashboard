import tornado.web
from ..settings import CHARTS
import gviz_api
from datetime import datetime


class ChartDataHandler(tornado.web.RequestHandler):
    def get(self):

        chart = CHARTS[self.get_argument('id')]


        # make query
        # chart['query']

        # map results

        buckets = [
            {'key': datetime.now(), 'doc_count': 4},
            {'key': datetime.now(), 'doc_count': 8},
            {'key': datetime.now(), 'doc_count': 12},
        ]

        schema = {
            "doc_count": ("number", "Сделок"),
            "key": ("datetime", "Дата")
        }

        table = gviz_api.DataTable(schema)
        table.LoadData(buckets)

        # TODO: CORS headers
        if self.get_argument('out', '') == 'simplejson':
            self.finish(table.ToJSon(columns_order=('key', 'doc_count')))
        else:
            self.finish(table.ToJSonResponse(columns_order=('key', 'doc_count'), req_id=0))



