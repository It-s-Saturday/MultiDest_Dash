import dash_bootstrap_components as dbc
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
            dbc.Input(
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

    alert_text = []
    if not origin:
        alert_text.append("origin")

    if not destination:
        alert_text.append("destination")

    s_parsed = [origin, destination]

    for i, stop in enumerate(stops):
        print(i, stop)
        if "value" in stop["props"]:
            if stop["props"]["value"] and len(stop["props"]["value"]) > 0:
                if stop["props"]["value"] not in s_parsed:
                    s_parsed.insert(-1, stop["props"]["value"])
                else:
                    return html.Div(
                        [
                            dbc.Alert(
                                [
                                    html.I(className="bi bi-info-circle-fill me-2"),
                                    f"Duplicate stop found at stop {i + 1}",
                                ],
                                color="info",
                                className="d-flex align-items-center",
                            )
                        ]
                    )
            else:
                alert_text.append(f"stop {i + 1}")
        else:
            alert_text.append(f"stop {i + 1}")

    if alert_text:
        return html.Div(
            [
                dbc.Alert(
                    [
                        html.I(className="bi bi-exclamation-triangle-fill me-2"),
                        f"Please enter {', '.join(alert_text)}",
                    ],
                    color="warning",
                    className="d-flex align-items-center",
                )
            ]
        )

    d = Driver(origin, destination, s_parsed[1:-1], "driving", method.lower())

    output = []

    for stop in d.best_path:
        output.append(html.P(stop))
    return [
        dbc.Toast(html.Div(output), className="mb-0", id="toast", header="Here is your path:", dismissable=True),
    ]
