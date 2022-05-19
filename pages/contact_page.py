from dash import Dash, html, dcc

layout = html.Div([

    # CONTACT US HEADER
    html.Div([
        html.Div(children='Contact Us', style={'color':'steelblue', 'font-weight':'bold', 'font-size':50}),
        html.Div(children="We'd love to hear from you!", style={'font-size':18}),
        html.Br(),   
    ], style={'text-align':'center'}),

    # EMAIL
    html.Div([
        html.H4(children="Email:", style={'font-weight':'bold'}),
        html.H6(children='its-saturday@gmail.com'),
        html.Br(),
    ]), 

    # GITHUB LINK
    html.Div([
        html.H4(children='Github:', style={'font-weight':'bold'}),
        html.A('Our code is open source. Check it out here!', href='https://github.com/It-s-Saturday/MultiDest_Dash', target='_blank'),
        html.Br(),
    ]),

    # FAQ
    html.Div([
        html.Br(),
        html.H4(children="FAQ:", style={'font-weight':'bold'}),
        html.H6(children="Is there a limit on how many stops can be added?", style={'color':'steelblue', 'font-weight':'bold'}),
        html.H6(children="No, you can add as much stops as you like!", style={'font-style':'italic'})
    ])
])