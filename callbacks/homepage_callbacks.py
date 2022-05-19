import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, callback, State, callback_context

@callback(
    Output("stops", "children"),
    Input("add-stop", "n_clicks"),
    Input("remove-stop", "n_clicks"),
    State("stops", "children"),
)
def update_stops(add_clicks, remove_clicks, children):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    print(children)
    if "add-stop" in changed_id:
        return children + [dcc.Input(id =f"stop_{add_clicks}", type = "text", placeholder = "Stop")]  
    elif "remove-stop" in changed_id:
        if len(children) > 0:
            children.pop()
            return children
        return []
    else:
        return []