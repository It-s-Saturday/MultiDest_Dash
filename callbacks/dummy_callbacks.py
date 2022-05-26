@app.callback(
    Output(component_id="result", type="value"),
    Input(component_id="origin", component_property="value"),
    Input(component_id="stop-list", component_property="value"),
    Input(component_id="destination", component_property="value"),
    Input(component_id="calculate-button", component_property="pressed"),
)
def update_output_div(origin, stoplist, destination, button):
    if not button:
        return dash.no_change
    return f"{origin} {stoplist} {destination}"
