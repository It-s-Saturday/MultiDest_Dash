from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        dcc.Store(id="store", storage_type="session"),
        html.Div(id="recalculate-alert", children=[]),
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
                        # html.Br(),
                        # html.Br(),
                        dbc.Accordion(
                            [
                                dbc.AccordionItem(
                                    [
                                        html.Div(
                                            [
                                                dbc.Label([html.H3("Metric")]),
                                                dbc.RadioItems(
                                                    id="input-metric",
                                                    options=[
                                                        {
                                                            "label": "Time",
                                                            "value": "time",
                                                        },
                                                        {
                                                            "label": "Distance",
                                                            "value": "distance",
                                                        },
                                                    ],
                                                    value="time",
                                                    inline=True,
                                                ),
                                            ],
                                            id="radio-container",
                                        ),
                                        html.Br(),
                                        html.Div(
                                            [
                                                dbc.Label([html.H3("Method")]),
                                                dbc.RadioItems(
                                                    id="input-method",
                                                    options=[
                                                        {
                                                            "label": "Driving",
                                                            "value": "driving",
                                                        },
                                                        {
                                                            "label": "Walking",
                                                            "value": "walking",
                                                        },
                                                        {
                                                            "label": "Biking",
                                                            "value": "bicycling",
                                                        },
                                                    ],
                                                    value="driving",
                                                    inline=True,
                                                ),
                                            ],
                                            id="radio-container2",
                                        ),
                                        html.Br(),
                                        html.Div(
                                            [
                                                dbc.Label([html.H3("Show converted?")]),
                                                html.Div(
                                                    [
                                                        dbc.Checklist(
                                                            options=[
                                                                {
                                                                    "label": "Show parsed",
                                                                    "value": 0,
                                                                },
                                                            ],
                                                            value=[0],
                                                            id="switches-input",
                                                            switch=True,
                                                        ),
                                                        html.Br(),
                                                    ],
                                                    id="toast-inner-container",
                                                ),
                                            ]
                                        ),
                                    ],
                                    title="More Options",
                                ),
                            ],
                        ),
                    ],
                    id="input-container",
                ),
            ]
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
                html.Div(id="alert-container"),
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
