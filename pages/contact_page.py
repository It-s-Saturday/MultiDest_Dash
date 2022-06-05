from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

d = {
    "name": {"placeholder": "Name", "label": "Name"},
    "email": {"placeholder": "example@gmail.com", "label": "Email"},
    "message": {"placeholder": "Message", "label": "Message"},
}

list_of_form_inputs = [
    html.Div(
        [
            dbc.Label("Name"),
            dbc.Input(
                id="form-name",
                type="text",
                placeholder="Name",
                autocomplete="false",
                autoFocus="true",
                required=True,
            ),
        ],
        className="mb-1",
    ),
    html.Div(
        [
            dbc.Label("Email"),
            dbc.Input(
                id="form-email",
                type="email",
                placeholder="Email Address",
                autoComplete="false",
                required=True,
            ),
        ],
        className="mb-1",
    ),
    html.Div(
        [
            dbc.Label("Message"),
            dbc.Textarea(
                id="form-message",
                placeholder="Message",
                required=True,
                style={"height": "200px"},
            ),
        ],
        className="mb-1",
    ),
]

form = dbc.Form(list_of_form_inputs)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    ["Contact Us"],
                    style={
                        "color": "steelblue",
                        "font-weight": "bold",
                        "font-size": 50,
                    },
                ),
            ],
            style={"text-align": "center", "margin-bottom": "1rem"},
        ),
        html.Div(
            [
                # LinkedIn
                html.Div(
                    [
                        html.H4(children="LinkedIn:", style={"font-weight": "bold"}),
                        dcc.Link(
                            ["https://www.linkedin.com/company/it-s-saturday/"],
                            href="https://www.linkedin.com/company/it-s-saturday/",
                            target="_blank",
                        ),
                        html.Br(),
                    ]
                ),
                html.Br(),
                # GITHUB LINK
                html.Div(
                    [
                        html.H4(children="Github:", style={"font-weight": "bold"}),
                        dcc.Link(
                            ["https://github.com/It-s-Saturday/MultiDest_Dash"],
                            href="https://github.com/It-s-Saturday/MultiDest_Dash",
                            target="_blank",
                        ),
                        html.Br(),
                    ]
                ),
                html.Div(
                    children="We'd love to hear from you!", style={"font-size": 18}
                ),
                html.Br(),
            ],
        ),
        form,
        dbc.Button("Submit", id="btn-submit"),
        html.Div(id="form-output"),
    ],
)
