from dash import html

layout = html.Div(
    [
        html.H1(children="Contact Us"),
        # INFO
        html.H3(children="Email: Its-Saturday@gmail.com"),
        html.A(
            "Github",
            href="https://github.com/It-s-Saturday/MultiDest_Dash",
            target="_blank",
        ),
        html.H2(children="FAQ:"),
    ]
)
