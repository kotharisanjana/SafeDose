import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .demographic_charts import generate_disposition_bubble, generate_casetype_sunburst, generate_episode_demographic_stacked_bar
from .drug_charts import generate_drug4_sunburst, generate_route_demographic_horizontal_bar
import pandas as pd

dash.register_page(__name__, path="/dashboard")

tab1 = html.Div(children=[
    dbc.Row([
        dbc.Col(generate_disposition_bubble(), width=5, className="dashboard-chart"),
        dbc.Col(generate_casetype_sunburst(), width=4, className="dashboard-chart")
    ], justify='around', className="dashboard-row"),
    dbc.Row([
        dbc.Col(generate_episode_demographic_stacked_bar(), width=5, className="dashboard-chart"),
    ], justify='around', className="dashboard-row")
])

tab2 = html.Div(children=[
    dbc.Row([
        dbc.Col(generate_drug4_sunburst(), width=4, className="dashboard-chart"),
        dbc.Col(generate_route_demographic_horizontal_bar(), width=5, className="dashboard-chart")
    ], justify='around', className="dashboard-row"),
])

layout = html.Div(children=[
    dcc.Tabs(id="tabs-for-graph", value='Demographic', children=[
        dcc.Tab(label='Demographic', children=[tab1], value='Demographic'),
        dcc.Tab(label='Drug-related', children=[tab2], value='Drug-related'),
    ])
])