import os
import time

import dash_bootstrap_components as dbc
from dash import Dash, html

from callbacks import homepage_callbacks, sidebar_callbacks
from layout import CONTENT_STYLE, layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "MultiDest"

print("rendering...")
server = app.server
start = time.time()

app.layout = html.Div(
    [
        layout,
    ],
    style=CONTENT_STYLE,
)
print(f"render complete {round(time.time() - start, 2)}s)")

if __name__ == "__main__":
    app.run_server(debug=True)
