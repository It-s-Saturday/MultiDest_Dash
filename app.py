import os
import time

import dash_bootstrap_components as dbc
from dash import Dash, html

from models.Timer import Timer
from callbacks import homepage_callbacks, sidebar_callbacks, contact_callbacks
from layout import CONTENT_STYLE, layout

with Timer("App Init") as t:
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "MultiDest"

    server = app.server
    start = time.time()

    app.layout = html.Div(
        [
            layout,
        ],
        style=CONTENT_STYLE,
    )
if __name__ == "__main__":
    app.run_server(debug=True)
