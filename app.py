# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import time

from layout import layout
from layout import CONTENT_STYLE, layout

from pages.contact import layout as layout_contact
from pages.dummy import layout as layout_dummy
from pages.home_page import layout as layout_home

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])    
print('rendering...')
server = app.server
start = time.time()

app.layout = html.Div([
    layout,
    layout_contact
    layout_home,
],
style=CONTENT_STYLE)

print(f'render complete {round(time.time() - start, 2)}s)')

if __name__ == '__main__':
    app.run_server(debug=True)
