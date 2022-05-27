import dash_bootstrap_components as dbc
from dash import dcc, html

from pages import home_page

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("MultiDest", className="display-4"),
        dbc.Fade(
            html.I("by It's Saturday"),
            id="subtitle-fade",
            class_name="text-muted",
            is_in=True,
            appear=True,
            style={"transition": "all 1.5s ease"},
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
                dbc.NavLink("Contact Us", href="/contact", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(
    [
        home_page.layout,
    ],  # Default on load is home_page
    id="page-content",
    style=CONTENT_STYLE,
)

layout = html.Div([dcc.Location(id="url"), sidebar, content])
