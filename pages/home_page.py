from dash import dcc, html

layout = html.Div(
    [
        html.Hgroup(children="Prioritize"),
        dcc.RadioItems(["Time", "Distance"], "Time", inline=True),
        dcc.Input(id="input-origin", type="text", placeholder="Origin"),
        html.Div(id="stops", children=[
            dcc.Input(id="stop-2", type="text", placeholder="Stop"),
            dcc.Input(id="stop-1", type="text", placeholder="Stop")
        ]),
        dcc.Input(id="input-destination", type="text", placeholder="Destination"),
        html.Button("Calculate", id="btn-calculate"),
        html.Div(id="container-button-basic"),
        html.Button("Add stop", id="add-stop"),
        html.Button("Remove Stop", id="remove-stop"),
        html.Div(id="output"),
    ]
)
