from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

layout = html.Div(
    [
        html.Hgroup(children='Prioritize'),
        dcc.Checklist(
            ['Time', 'Distance'],
            inline=True
        ),
        dcc.Input(
            id="input_Origin",
            type="text",
            placeholder="Origin"
        ),
        dcc.Input(
            id="input_Stops",
            type="text",
            placeholder="Stops"
        ),
        dcc.Input(
            id="input_Destination",
            type="text",
            placeholder="Destination"
        ),
        html.Button('Calculate'),
        html.Div(id='container-button-basic')
    ]
)
