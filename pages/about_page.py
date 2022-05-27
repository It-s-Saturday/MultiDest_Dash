import base64
import os

from dash import html

Div = html.Div(
    [
        html.H1("What is MultiDest"),
        html.Div(
            [
                html.P("Multidest is a new way for people to get "),
                html.P("....... !!!!"),
                html.P(""),
            ]
        ),
        html.H2("How does it work"),
        html.Div(
            [
                html.P("......."),
                html.P("........"),
            ]
        ),
    ]
)

image_filename = os.getcwd() + "/assets/AM.png"  # replace with your own image
# print(image_filename)


def b64_image(image_filename):
    with open(image_filename, "rb") as f:
        image = f.read()
    return "data:image/png;base64," + base64.b64encode(image).decode("utf-8")


image = html.Img(src=b64_image(image_filename))
layout = html.Div([image, Div])
