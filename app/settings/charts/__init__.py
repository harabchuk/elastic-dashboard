from .sales import chart as sales_chart
from .regions import chart as regions_chart

CHARTS = {
    sales_chart['id']: sales_chart,
    regions_chart['id']: regions_chart
}