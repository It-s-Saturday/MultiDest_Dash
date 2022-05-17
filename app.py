from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import time

from layout import layout
from layout import CONTENT_STYLE, layout
from callbacks import sidebar_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
print('rendering...')
server = app.server
start = time.time()

app.layout = html.Div([
    layout,
],
    style=CONTENT_STYLE
)

print(f'render complete {round(time.time() - start, 2)}s)')

if __name__ == '__main__':
    app.run_server(debug=True)
