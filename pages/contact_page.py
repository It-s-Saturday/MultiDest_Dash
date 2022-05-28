from dash import Dash, html, dcc

layout = html.Div(
    [
        # CONTACT US HEADER
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
                html.Div(
                    children="We'd love to hear from you!", style={"font-size": 18}
                ),
                html.Br(),
            ],
            style={"text-align": "center"},
        ),
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
    ]
)
