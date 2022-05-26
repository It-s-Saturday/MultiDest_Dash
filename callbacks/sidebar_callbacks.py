import dash_bootstrap_components as dbc
from dash import Input, Output, html, callback
from pages import about_page, contact_page, dummy_page, home_page


@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(url_endpoint):
    if url_endpoint == "/":
        return home_page.layout
    elif url_endpoint == "/about":
        return about_page.layout
    elif url_endpoint == "/contact":
        return contact_page.layout
    elif url_endpoint == "/dummy":
        return dummy_page.layout
    else:
        return None
