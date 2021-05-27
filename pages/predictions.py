# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_html_components as html
import pandas as pd
import numpy as np
from joblib import load

# Imports from this application
from app import app

# load model trained on airbnb data
model_rf = load('assets/predictor.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout



column1 = dbc.Col([
            dcc.Markdown("###### City"),
            dcc.Dropdown(
                id='city',
                options=[
                {'label': 'NYC', 'value': 'NYC'},
                {'label': 'SF', 'value': 'SF'},
                {'label': 'DC', 'value': 'DC'},
                {'label': 'LA', 'value': 'LA'},
                {'label': 'Chicago', 'value': 'Chicago'},
                {'label': 'Boston', 'value': 'Boston'},
                ],
                value='SF',
                className='mb-4',
                style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
            ), 

            dcc.Markdown("###### Instant Booking?"),
            dcc.Dropdown(
                id='instant_bookable',
                options=[
                {'label': 'False', 'value': 'f'},
                {'label': 'True', 'value': 't'},
                ],
                value='t',
                className='mb-4',
                style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
            ),
      
            html.Div([

                dcc.Markdown("###### Select Bed Type"),
                dcc.Dropdown(
                    id='bed_type',
                    options=[
                        {'label': 'Real Bed', 'value': 'Real Bed'},
                        {'label': 'Futon', 'value': 'Futon'},
                        {'label': 'Pull-out Sofa', 'value': 'Pull-out Sofa'},
                        {'label': 'Couch', 'value': 'Couch'},
                        {'label': 'Airbed', 'value': 'Airbed'},
                    ],
                        value='Real Bed',
                        className='mb-4',
                        style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
                ), 
                    
                dcc.Markdown("###### Property_Type"),
                dcc.Dropdown(
                    id='property_type',
                    options=[
                    {'label': 'Apartment', 'value': 'Apartment'},
                    {'label': 'House', 'value': 'House'},
                    {'label': 'Condominium', 'value': 'Condominium'},
                    {'label': 'Loft', 'value': 'Loft'},
                    {'label': 'Townhouse', 'value': 'Townhouse'},
                    {'label': 'Bed & Breakfast', 'value': 'Bed & Breakfast'},
                    {'label': 'Bungalow', 'value': 'Bungalow'},
                    {'label': 'Guesthouse', 'value': 'Guesthouse'},
                    {'label': 'Dorm', 'value': 'Dorm'},
                    {'label': 'Other', 'value': 'Other'},
                    {'label': 'Camper/RV', 'value': 'Camper/RV'},
                    {'label': 'Hostel', 'value': 'Hostel'},
                    {'label': 'Villa', 'value': 'Villa'},
                    {'label': 'Boutique hotel', 'value': 'Boutique hotel'},
                    {'label': 'Timeshare', 'value': 'Timeshare'},
                    {'label': 'In-law', 'value': 'In-law'},
                    {'label': 'Boat', 'value': 'Boat'},
                    {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
                    {'label': 'Castle', 'value': 'Castle'},
                    {'label': 'Cabin', 'value': 'Cabin'},
                    {'label': 'Treehouse', 'value': 'Treehouse'},
                    {'label': 'Tipi', 'value': 'Tipi'},
                    {'label': 'Vacation home', 'value': 'Vacation home'},
                    {'label': 'Tent', 'value': 'Tent'},
                    {'label': 'Hut', 'value': 'Hut'},
                    {'label': 'Casa particular', 'value': 'Casa particular'},
                    {'label': 'Chalet', 'value': 'Chalet'},
                    {'label': 'Yurt', 'value': 'Yurt'},
                    {'label': 'Earth House', 'value': 'Earth House'},
                    {'label': 'Parking Space', 'value': 'Parking Space'},
                    {'label': 'Train', 'value': 'Train'},
                    {'label': 'Cave', 'value': 'Cave'},
                    {'label': 'Lighthouse', 'value': 'Lighthouse'},
                    {'label': 'Island', 'value': 'Island'},
                    ],
                    value='Apartment',
                    className='mb-4',
                    style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
                    ), 


                dcc.Markdown("###### Room Type"),
                dcc.Dropdown(
                    id='room_type',
                    options=[
                        {'label': 'Entire home/apt', 'value': 'Entire home/apt'},
                        {'label': 'Private room', 'value': 'Private room'},
                        {'label': 'Shared room', 'value': 'Shared room'}
                    ],
                    value='Private room',
                    className='mb-4',
                    style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
                )

                ])
		],md=3) 


column2 = dbc.Col([
            dcc.Markdown("###### Number of Bedrooms", className='mb-1'),
            daq.NumericInput(
                id='bedrooms', 
                min=0,
                max=6,
                value=1,
                className='mb-4',
            ),

            dcc.Markdown("###### Number of Beds", className='mb-1'),
            daq.NumericInput(
                id='beds',
                min=0,
                max=6,
                value=1,
                className='mb-4',
            ),

            dcc.Markdown("###### Number of Bathrooms", className='mb-1'),
	        daq.NumericInput(
                id='bathrooms',
                min=0,
                max=3,
                value=1,
                className='mb-4',
            ),

            html.Div([
                dcc.Markdown("###### Cancellation Policy"),
                    dcc.Dropdown(
                        id='cancellation_policy',
                        options=[
                            {'label': 'strict', 'value': 'strict'},
                            {'label': 'moderate', 'value': 'moderate'},
                            {'label': 'flexible', 'value': 'flexible'},
                            {'label': 'super strict(30)', 'value': 'super strict(30)'},
                            {'label': 'super strict(60)', 'value': 'super strict(60)'},
                        ],
                            value='moderate',
                            className='mb-4',
                            style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
                    ),

            dcc.Markdown("###### Are you a verified host?"),
            dcc.Dropdown(
                id='host_identity_verified',
                options=[
                    {'label': 'False', 'value': 'f'},
                    {'label': 'True', 'value': 't'},
                ],
                value='t',
                className='mb-4',
                style={'fontFamily':'Verdana', 'fontWeight': 'normal'}
                )
            ]),
            ],md=3)

column3 = dbc.Col([
        dcc.Markdown('### Your Rental price ($)'),
        daq.LEDDisplay(
            id='prediction-content',
            size=45,
            color="#262626"),
        

            html.Img(src='assets/airbnb4.jpeg', className='img-fluid')
        ]
)


@app.callback(
	
    Output('prediction-content', 'value'),
        [
            Input('city', 'value'),
            Input('instant_bookable', 'value'),
            Input('property_type', 'value'),
            Input('room_type', 'value'),
            Input('host_identity_verified', 'value'),
            Input('bedrooms', 'value'),
            Input('beds', 'value'),
            Input('bathrooms', 'value'),
            Input('bed_type', 'value'),
            Input('cancellation_policy', 'value')
 
        ]
    )

def predict(city, instant_bookable, property_type, room_type, host_identity_verified,
            bedrooms, beds, bathrooms, bed_type, cancellation_policy
            ):
    df = pd.DataFrame(
        columns=['city', 'instant_bookable', 'property_type', 'room_type', 'host_identity_verified',   
             'bedrooms', 'beds', 'bathrooms', 'bed_type','cancellation_policy'],
        data=[[city, instant_bookable, property_type, room_type, host_identity_verified,   
            bedrooms, beds, bathrooms,  bed_type, cancellation_policy]])
    
    y_pred = round(np.exp(model_rf.predict(df)[0]),2)
    
    return y_pred

layout = dbc.Row([column1, column2, column3])
