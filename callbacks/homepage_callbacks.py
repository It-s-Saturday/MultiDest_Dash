from dash import Input, Output, State, callback, callback_context, dcc, html, no_update
from logic.driver import Driver
from models import InputStore, Timer

stop_counter = 0


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
   
    stop_counter = len(children) + 1
    
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    
    if "add-stop" in changed_id:
        return children + [
            dcc.Input(
                id=f"stop_{add_clicks}", type="text", placeholder=f"Stop {stop_counter}"
            )
        ]
    elif "remove-stop" in changed_id:
        if len(children) > 2:
            children.pop()
            return children
        return children
    else:
        return []


@callback(
    Output("output", "children"),
    [
        Input("btn-calculate", "n_clicks"),
        State("input-origin", "value"),
        State("input-destination", "value"),
        State("stops", "children"),
        State("input-metric", "value"),
    ],
)
def update_output(n_clicks, origin, destination, stops, method):
    if n_clicks is None:
        return no_update

    s_parsed = []
    for i, stop in enumerate(stops):
        try:
            if stop["props"]["value"] not in s_parsed:
                s_parsed.append(stop["props"]["value"])
            else:
                raise Exception("Possible duplicate value")
        except Exception as e:
            return html.Div(
                f"{f'Error: {e} ' if e else ''}Please enter a valid stop! (Stop {i+1}) "
            )
    d = Driver(origin, destination, s_parsed, "driving", method.lower())
    return [
        html.Div(f"Route: {d.best_path}"),
    ]
