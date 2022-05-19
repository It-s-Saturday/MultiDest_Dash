from dash import Dash, html, dcc, callback, callback_context
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from callbacks import homepage_callbacks

layout = html.Div(
    [
    html.Hgroup(children = 'Prioritize'),
    dcc.Checklist(
    ['Time', 'Distance'],
    inline=True
    ),
    dcc.Input(
            
            id="input-origin",
            type = "text",
            placeholder = "Origin"
        
        ),
    
        html.Div(
            id="stops",
            children=[]
        ),
        # html.Button('Add another Stop'),
        # html.Div(id='container-button-basic'),
        dcc.Input(
            id ="input-destination",
            type = "text",
            placeholder = "Destination"

        ),
    html.Button('Calculate'),
    html.Div(id='container-button-basic'),
    html.Button("Add Stop", id="add-stop", n_clicks=0),
    html.Button("Remove Stop", id="remove-stop")
    ]
)



