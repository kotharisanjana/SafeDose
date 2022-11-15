import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .demographic_charts import generate_age_disposition, generate_casetype_sunburst
import pandas as pd

dash.register_page(__name__, path="/dashboard")

tab1 = html.Div(children=[
    dbc.Row([
        dbc.Col(generate_age_disposition(), width=4),
        dbc.Col(generate_casetype_sunburst(), width=4)
    ])
])

tab2 = html.Div(children=[
    html.H3('Tab2')
])

layout = html.Div(children=[
    dcc.Tabs(id="tabs-example-graph", value='Demographic', children=[
        dcc.Tab(label='Demographic', children=[tab1], value='Demographic'),
        dcc.Tab(label='Drug-related', children=[tab2], value='Drug-related'),
    ])
])