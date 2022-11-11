import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

dataframe = pd.read_csv('assets/demographic_data.csv')

def generate_age_disposition():
    fig = px.scatter(dataframe, x="AGECAT", y="DISPOSITION")

    return html.Div(children=[
        dcc.Graph(id='age-disposition', figure=fig
    )])

def generate_metro_cases():
    return html.Div(children=[
        html.Label('Select one'),
        dcc.Dropdown(['SEX', 'RACE', 'METRO'], 'METRO', id='casetype-sunburst-dropdown'),
        dcc.Graph(id='casetype-sunburst-graph')
    ])

@dash.callback(Output('casetype-sunburst-graph', 'figure'), Input('casetype-sunburst-dropdown', 'value'))
def update_figure(selected_column):
    df_grouped = dataframe.groupby([selected_column, 'CASETYPE']).agg(
    count_col=pd.NamedAgg(column='CASETYPE', aggfunc="count")
        )
    df_grouped = df_grouped.reset_index()
    fig = px.sunburst(df_grouped,
        path=[selected_column, "CASETYPE"],
        values='count_col',
        title=f"CASETYPE distribution(counts of cases with this casetype) in each {selected_column}",
        width=750, height=750)


    return fig