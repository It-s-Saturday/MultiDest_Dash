import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import base64
import dash_html_components as html

image_filename = os.getcwd()+'/pages/AM.png'  # replace with your own image
print(image_filename)


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


layout = html.Img(src=b64_image(image_filename))
