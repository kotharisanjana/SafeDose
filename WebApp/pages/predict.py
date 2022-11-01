import dash
from dash import html, dcc

dash.register_page(__name__, path="/predict")

layout = html.Div(children=[
    html.H1(children='Form for prediction')
])