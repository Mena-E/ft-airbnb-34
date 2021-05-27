# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### How much is your property worth?
            
            
            This app is built to help hosts predict the price of their listing daily.
            """,
            style={'fontFamily':'Verdana', 'fontWeight': 'normal', 'fontSize': 'smaller'}
        ),
        dcc.Link(dbc.Button('Predict That Price', color='primary'), href='/predictions'),

    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.Img(src='https://images.unsplash.com/photo-1621963262756-6836c6c86d27?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=728&q=80', style={'width': '100%'})
    ]
)

layout = dbc.Row([column1, column2])
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training