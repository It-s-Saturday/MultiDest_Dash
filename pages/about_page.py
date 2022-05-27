import base64
import os

from dash import html
import dash_bootstrap_components as dbc

Div = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Background"),
                        html.Div(
                            [
                                html.P(
                                    "MultiDest solves route optimization by minimizing travel \
                            metric across many stops. In taking an origin, 2-10 stops, and a destination,\
                            MultiDest returns the shortest path, hitting every intermediate stop."
                                ),
                            ]
                        ),
                    ],
                    id="background-div",
                ),
                html.Div(
                    [
                        html.H2("Implementation"),
                        html.Div(
                            [
                                html.P(
                                    "We used the comprehensive Traveling Salesman Problem (TSP) \
                            algorithm to solve the problem. By constructing an adjaceny list of:"
                                ),
                                dbc.ListGroup(
                                    [
                                        dbc.ListGroupItem("Origin -> All stops"),
                                        dbc.ListGroupItem(
                                            "All stops -> each other and destination"
                                        ),
                                    ],
                                    style={"width": "20rem"},
                                ),
                                html.P(
                                    "we use our optimized TSP algorithm to find the shortest path."
                                ),
                            ]
                        ),
                    ],
                    id="how-div",
                ),
                html.Div(
                    [
                        html.H2("FAQ"),
                        dbc.Accordion(
                            [
                                dbc.AccordionItem(
                                    [
                                        html.P(
                                            "Because of a runtime complexity of O(n! - m) where n is the number of stops \
                                            and m is the number paths whose calculation terminates early,\
                                            we set the cutoff to 10 stops to limit Google API calls and \
                                            for user experience."
                                        ),
                                    ],
                                    title="Why is the cutoff 10 stops?",
                                ),
                                dbc.AccordionItem(
                                    [
                                        html.P(
                                            "In calculating the cost of each path, first we establish\
                                            a list of all valid paths. These are paths that have the origin and destination\
                                            in the correct positions. Second, we construct an adjacency list of the \
                                            metrics between all the valid intermediate stops. Third, we calculate \
                                            the cost of each path by summing the metrics between the origin, stops,\
                                            and destination. The optimization here is that if the current path already\
                                            exceeds the minimum cost, we can skip the rest of the calculation and check the next path."
                                        ),
                                        html.P(
                                            "We utilize the concept of dynamic programming to reduce the number of calls to the Google API.\
                                            By storing the results of the previous calculation in the adjacency list, we can skip the API call \
                                                each time that combination of stops is encountered. This also applies the the name_lookup function \
                                                    which is used to convert the user input to parsed input."
                                        ),
                                    ],
                                    title="How is this implementation optimized?",
                                ),
                            ],
                            start_collapsed=True,
                            always_open=True
                        ),
                    ]
                ),
            ],
            # center div on the page
            style={"width": "30rem"},
            className="mx-auto",
        )
    ],
)

image_filename = (
    os.getcwd() + "/assets/multidestlogo.png"
)  # replace with your own image
# print(image_filename)


def b64_image(image_filename):
    with open(image_filename, "rb") as f:
        image = f.read()
    return "data:image/png;base64," + base64.b64encode(image).decode("utf-8")


image = html.Div(
    [
        html.Img(
            src=b64_image(image_filename),
            style={"width": "30rem", "margin": "0"},
        )
    ],
    style={"text-align": "center"},
)
layout = html.Div([image, Div])
