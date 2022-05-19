from dash import Input, Output, State, callback, callback_context, dcc, html, no_update


@callback(
    Output("stops", "children"),
    [
        Input("add-stop", "n_clicks"),
        Input("remove-stop", "n_clicks"),
        State("stops", "children"),
    ],
)
def update_stops(add_clicks, remove_clicks, children):
    if add_clicks is None and remove_clicks is None:
        return no_update
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    print(children)
    print(changed_id)
    if "add-stop" in changed_id:
        return children + [
            dcc.Input(id=f"stop_{add_clicks}", type="text", placeholder="Stop")
        ]
    elif "remove-stop" in changed_id:
        if len(children) > 0:
            children.pop()
            return children
        return []
    else:
        return []


@callback(
    Output("output", "children"),
    [
        Input("btn-calculate", "n_clicks"),
        State("input-origin", "value"),
        State("input-destination", "value"),
        State("stops", "children"),
    ],
)
def update_output(n_clicks, origin, destination, stops):
    if n_clicks is None:
        return no_update

    def stops_to_list(stops):
        return [stop['props']['value'] for stop in stops]

    s_parsed = stops_to_list(stops)
    return [
        html.Div(f"Origin: {origin}"),
        html.Div(f"Destination: {destination}"),
        html.Div(f"Stops: {s_parsed}"),
    ]
