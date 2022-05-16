
from cgitb import text
from re import A
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

layout = html.Div(
    [
    dcc.Input(
            
            id="input_Origin",
            type = "text",
            placeholder = "Origin"
        
        ),
    ]
)
