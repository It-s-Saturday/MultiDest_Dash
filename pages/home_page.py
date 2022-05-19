from dash import dcc, html

layout = html.Div(
    [
        html.Hgroup(children="Prioritize"),
        dcc.RadioItems(["Time", "Distance"], "Time", inline=True),
        dcc.Input(id="input-origin", type="text", placeholder="Origin"),
        html.Div(id="stops", children=[]),
        # html.Button('Add another Stop'),
        # html.Div(id='container-button-basic'),
        dcc.Input(id="input-destination", type="text", placeholder="Destination"),
        html.Button(id="btn-calculate", value="Calculate"),
        html.Div(id="container-button-basic"),
        html.Button(id="add-stop", value="Add Stop"),
        html.Button(id="remove-stop", value="Remove Stop"),
        html.Div(id="output"),
    ]
)
