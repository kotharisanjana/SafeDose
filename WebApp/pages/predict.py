import dash
from dash import html, dcc
from .all_abuse_form import generate_all_abuse_prediction

dash.register_page(__name__, path="/predict")


layout = html.Div(children=[
     generate_all_abuse_prediction()   
], className='predict-container')