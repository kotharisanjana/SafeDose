import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .demographic_charts import generate_age_disposition, generate_metro_cases
import pandas as pd

dash.register_page(__name__, path="/dashboard")

tab1 = html.Div(children=[
    dbc.Row([
        dbc.Col(generate_age_disposition(), width=4),
        dbc.Col(generate_metro_cases(), width=4)
    ])
])

tab2 = html.Div(children=[
    html.H3('Tab2')
])

layout = html.Div(children=[
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Tab One',children=[tab1]),
        dcc.Tab(label='Tab Two', children=[tab2]),
    ])
])