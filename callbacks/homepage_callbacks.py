from datetime import datetime, timedelta

import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, callback_context, dcc, html, no_update
from logic.driver import Driver
from models import InputStore, Timer

stop_counter = 0

@callback(
    [
        Output("stops", "children"),
        Output("alert-container", "children"),
    ],
    [
        Input("add-stop", "n_clicks"),
        Input("remove-stop", "n_clicks"),
        State("stops", "children"),
    ],
)
def update_stops(add_clicks, remove_clicks, children):
    if add_clicks is None and remove_clicks is None:
        return no_update, no_update

    stop_counter = len(children) + 1

    changed_id = [p["prop_id"] for p in callback_context.triggered][0]

    if "add-stop" in changed_id:
        if len(children) > 9:
            return children, dbc.Alert(
                "Algorithm not optimized for more than 10 stops!",
                color="warning",
                is_open=True,
                duration=2000,
            )
        return (
            (
                children
                + [
                    dbc.Input(
                        id=f"stop_{add_clicks}",
                        type="text",
                        placeholder=f"Stop {stop_counter}",
                    )
                ]
            ),
            no_update,
        )

    elif "remove-stop" in changed_id:
        if len(children) > 2:
            children.pop()
            return children, no_update
        return children, dbc.Alert(
            "You must have at least 2 stops",
            color="info",
            is_open=True,
            duration=2000,
        )
    else:
        return []


INTERMEDIATE_STYLE = {
    # "font-style": "italic",
    "color": "gray",
    "padding": "0",
    "margin": "0",
}

STOP_STYLE = {
    "padding": "0",
    "margin": "0",
}

OUTPUT_TEXT_STYLE = {
    # "padding": "1vw",
    "font-style": "italic",
    "margin": "1vw",
}


# @callback(
#     Output("output", "children"),
#     [Input("switches-input", "value"), State("store", "data")],
# )
# def switch_between_user_and_parsed(switched, store):
#     if not store or len(store) != 2:
#         return dash.no_update

#     if switched:
#         return store["parsed_output"]

#     return store["user_input"]


@callback(
    [
        Output("output", "children"),
        Output("store", "data"),
    ],
    [
        Input("btn-calculate", "n_clicks"),
        State("input-origin", "value"),
        State("input-destination", "value"),
        State("stops", "children"),
        State("input-method", "value"),
        State("input-metric", "value"),
        Input("switches-input", "value"),
        State("store", "data"),
    ],
)

def update_output(
    n_clicks, origin, destination, stops, method, metric, switched, store_in
):

    original_method = method
    original_metric = metric

    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    if n_clicks is None or "btn-calculate" not in changed_id:
        if "switches-input" in changed_id:
            if switched:
                return store_in["parsed_input"], store_in
            return store_in["user_input"], store_in

        return no_update

    alert_text = []
    if not origin:
        alert_text.append("origin")

    if not destination:
        alert_text.append("destination")

    s_parsed = [origin, destination]

    for i, stop in enumerate(stops):
        # print(i, stop)
        if "value" in stop["props"]:
            if stop["props"]["value"] and len(stop["props"]["value"]) > 0:
                if stop["props"]["value"] not in s_parsed:
                    s_parsed.insert(-1, stop["props"]["value"])
                else:
                    return html.Div(
                        children=[
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
            children=[
                dbc.Alert(
                    [
                        html.I(className="bi bi-exclamation-triangle-fill me-2"),
                        f"Please enter {', '.join(alert_text)}",
                    ],
                    color="warning",
                    className="d-flex align-items-center",
                    duration=2000,
                )
            ]
        )

    d = Driver(
        origin, destination, s_parsed[1:-1], method=method, metric=metric.lower()
    )

    def create_output(using):
        output = []
        for i, stop in enumerate(using):
            output.append(html.P(stop, style=STOP_STYLE))

            if i < len(using) - 1:
                # print(metric)
                metric_val = d.adj_matrix[d.parsed_best_path[i]][
                    d.parsed_best_path[i + 1]
                ]
                if metric == "distance":
                    metric_suffix = "mi"
                elif metric == "time":
                    if metric_val > 1:
                        metric_suffix = "mins"
                    else:
                        metric_suffix = "min"
                else:
                    metric_suffix = "?"
                output.append(
                    html.Pre(
                        [f"|  {metric_val}{metric_suffix}"], style=INTERMEDIATE_STYLE
                    )
                )
        text_metric, eta = "", ""
        if metric == "time":
            text_metric = "minute(s)"
            calculated_eta = datetime.now() + timedelta(minutes=d.cost)
            eta = f" ETA: {calculated_eta.strftime('%H:%M')}"
        elif metric == "distance":
            text_metric = "mile(s)"

        output.append(
            html.P(
                f"This route is {d.cost} {text_metric} long.{eta}",
                style=OUTPUT_TEXT_STYLE,
            )
        )

        return output

    store = {
        "user_input": create_output(d.best_path),
        "parsed_input": create_output(d.parsed_best_path),
    }

    if switched:
        output = store["parsed_input"]
    else:
        output = store["user_input"]

    return [
        dbc.Toast(
            html.Div(output),
            className="mb-0",
            id="toast",
            header="Here is your path:",
            dismissable=True,
            style={"width": "100%"},
        ),
        store,
    ]


@callback(
    Output("url", "hash"),
    [Input("btn-calculate", "n_clicks"), Input("toast", "header")],
)
def update_href(n_clicks, _):
    if n_clicks is None:
        return no_update
    if n_clicks > 0:
        return "#output"
    return no_update

@callback(
    Output("recalculate-alert", "children"),
    [
        Input("input-method", "value"),
        Input("input-metric", "value"),
        Input("url", "hash")
    ]
)
def update_alerts(method, metric, hash):
    if hash == "#output":
        changed_id = [p['prop_id'] for p in callback_context.triggered][0]
        print(changed_id)
        if not changed_id:
            return None
        if changed_id == "input-metric.value" or changed_id == "input_method.value":
            return dbc.Alert("You must recalculate to see changes.", color="info", duration=3000)
    else:
        return None
