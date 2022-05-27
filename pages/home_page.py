from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dbc.Label([html.H3("Inputs")]),
                            html.Div(
                                children=[
                                    # dbc.Label("Origin"),
                                    dbc.Input(
                                        id="input-origin",
                                        type="text",
                                        placeholder="Origin",
                                        style={"width": "100%"},
                                    ),
                                    html.Br(),
                                ]
                            ),
                            html.Div(
                                children=[
                                    # dbc.Label("Stops"),
                                    html.Div(
                                        id="stops",
                                        children=[
                                            dbc.Input(
                                                id="stop-1",
                                                type="text",
                                                placeholder="Stop 1",
                                                style={"width": "100%"},
                                            ),
                                            dbc.Input(
                                                id="stop-2",
                                                type="text",
                                                placeholder="Stop 2",
                                                style={"width": "100%"},
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        children=[
                                            dbc.Button(
                                                "Add stop",
                                                color="secondary",
                                                id="add-stop",
                                            ),
                                            dbc.Button(
                                                "Remove Stop",
                                                color="secondary",
                                                id="remove-stop",
                                            ),
                                        ],
                                        id="add-remove-button-container",
                                    ),
                                ]
                            ),
                            html.Br(),
                            html.Div(
                                children=[
                                    # dbc.Label("Destination"),
                                    dbc.Input(
                                        id="input-destination",
                                        type="text",
                                        placeholder="Destination",
                                        style={"width": "100%"},
                                    ),
                                    html.Br(),
                                ]
                            ),
                        ],
                    ),
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.Label([html.H3("Metric")]),
                                dbc.RadioItems(
                                    id="input-metric",
                                    options=[
                                        {"label": "Time", "value": "time"},
                                        {"label": "Distance", "value": "distance"},
                                    ],
                                    value="time",
                                    # inline=True,
                                ),
                            ],
                            id="radio-container",
                        ),
                        html.Br(),
                    ]
                ),
            ],
            id="input-container",
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        dbc.Button(
                            "Calculate", id="btn-calculate", style={"width": "100%"}
                        ),
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
        ),
    ]
)
