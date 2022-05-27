from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        html.Div(
            [
                dbc.Label("Calculate"),
                dbc.RadioItems(
                    id="input-metric",
                    options=[
                        {"label": "Time", "value": "time"},
                        {"label": "Distance", "value": "distance"},
                    ],
                    value="time",
                    inline=True,
                ),
            ],
            id="radio-container",
        ),
        html.Div(
            [
                html.Div(
                    children=[
                        dbc.Label("Origin"),
                        dbc.Input(id="input-origin", type="text", placeholder="Origin"),
                        html.Hr(),
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Label("Stops"),
                        html.Div(
                            id="stops",
                            children=[
                                dbc.Input(
                                    id="stop-1", type="text", placeholder="Stop 1"
                                ),
                                dbc.Input(
                                    id="stop-2", type="text", placeholder="Stop 2"
                                ),
                            ],
                        ),
                    ]
                ),
                html.Hr(),
                html.Div(
                    children=[
                        dbc.Label("Destination"),
                        dbc.Input(
                            id="input-destination",
                            type="text",
                            placeholder="Destination",
                        ),
                        html.Br(),
                    ]
                ),
            ],
            id="input-container",
        ),
        html.Div(
            [
                html.Div(
                    children=[
                        dbc.Button("Add stop", color="secondary", id="add-stop"),
                        dbc.Button("Remove Stop", color="secondary", id="remove-stop"),
                    ],
                    id="add-remove-button-container",
                ),
                dbc.Button("Calculate", id="btn-calculate"),
            ]
        ),
        html.Div(
            [
                dbc.Spinner(
                    html.Div(id="output"),
                    delay_hide=100,
                    delay_show=100,
                    show_initially=False,
                ),
            ]
        ),
    ]
)
