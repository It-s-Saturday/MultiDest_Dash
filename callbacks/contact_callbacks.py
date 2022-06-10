import re

import dash_bootstrap_components as dbc
import yagmail
import os
from dash import Input, Output, State, callback, callback_context, dcc, html, no_update

if os.path.exists("./models/secret.py"):
    from models.secret import *
else:
    PASSWORD = os.environ["PASSWORD"]
    USERNAME = os.environ["USERNAME"]

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


@callback(
    Output("form-output", "children"),
    [
        Input("form-name", "value"),
        Input("form-email", "value"),
        Input("form-message", "value"),
        Input("btn-submit", "n_clicks"),
    ],
)
def submit_form(form_name, form_email, form_message, btn_pressed):
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    if "btn-submit" not in changed_id:
        return no_update

    if not form_name:
        return dbc.Alert("Name is required", color="danger")

    if not form_email:
        return (
            dbc.Alert(
                "Please enter your email address.",
                color="danger",
                style={"margin-bottom": "1rem"},
            ),
        )

    def isValid(email):
        return re.fullmatch(regex, email)

    if not isValid(form_email):
        return dbc.Alert("Please enter a valid email address.", color="danger")

    if not form_message:
        return (
            dbc.Alert(
                "Please enter your message.",
                color="danger",
                style={"margin-bottom": "1rem"},
            ),
        )
    try:
        yag = yagmail.SMTP(USERNAME, PASSWORD)
    except:
        return dbc.Alert(
            "Error in establishing SMTP",
            color="danger",
            style={"margin-bottom": "1rem"},
        )
    try:
        yag.send(USERNAME, f"[MultiDest] - {form_name}", f'{form_message}\n\n{form_email}')

    except Exception as e:
        print(e)
        return dbc.Alert(
            "Error in sending email",
            color="danger",
            style={"margin-bottom": "1rem"},
        )

    return dbc.Alert(
        "Your message has been sent!",
        color="success",
        style={"margin-bottom": "1rem"},
    )
