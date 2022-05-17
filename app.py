# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

from layout import layout
from pages.contact import layout as layout_contact

app = Dash(__name__)
                         
app.layout = html.Div([
    layout,
    layout_contact
])
if __name__ == '__main__':
    app.run_server(debug=True)
