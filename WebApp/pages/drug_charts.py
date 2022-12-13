import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dataframe_drug = pd.read_csv('assets/drug4_data.csv', index_col=0)
dataframe_route = pd.read_csv('assets/routes_data.csv', index_col=0)
dataframe_demographic = pd.read_csv('assets/demographic_data.csv')

AGECAT_map = {0:'NA', 1:'<= 5', 2:'6-11',3:'12-17', 4:'18-20', 5:'21-24', 6:'25-29', 7:'30-34', 8:'35-44', 9:'45-54', 10:'55-64',11:'>= 65'}
SEX_map = {0:'NA', 1:'Male', 2:'Female'}
RACE_map = {0:'NA', 1:'White', 2:'Black/African American',3:'Any Hispanic/Latino', 4:'All Other'}
METRO_map = {0:'NA', 1:'MA-NH', 2:'NY-NJ-PA',3:'IL-IN-WI', 4:'MI', 5:'MN-WI', 6:'FL', 7:'FL', 8:'TX', 9:'CO', 10:'AZ',11:'CA', 12:'CA', 13:'WA', 14:'Other'}
CASETYPE_map = {0: 'NA', 1:'Suicide Attempt', 2:'Seeking Detox',3:'Alcohol Only(Age<21)', 4:'Adverse Reaction', 5:'Overmedication', 6:'Malicious Poisoning', 7:'Accidental Injestion', 8:'Other'}
DISPOSITION_map = {0:'NA', 1:'Discharged home', 2:'Released to police/Jail',3:'Referred to detox/Treatment', 4:'ICU/Critical care', 5:'Surgery', 6:'Chemical dependency/detox, Psychiatric unit', 7:'Other inpatient unit', 8:'Transferred', 9:'Left agaist medical advice', 10:'Died',11:'Other'}

demographic_column_map = {
    'Gender': {
        'column':'SEX',
        'map': SEX_map
    }, 
    'Age': {
        'column':'AGECAT',
        'map': AGECAT_map
    },    
    'Race': {
        'column':'RACE',
        'map': RACE_map
    },    
    'Metro': {
        'column':'METRO',
        'map': METRO_map
    },   
}

def generate_drug4_sunburst():
    dropdown_labels = list(demographic_column_map.keys())
    return html.Div(children=[
        html.Label('Select one'),
        dcc.Dropdown(dropdown_labels, dropdown_labels[0], id='drug4-sunburst-dropdown', clearable=False),
        dcc.Graph(id='drug4-sunburst-graph')
    ])

@dash.callback(Output('drug4-sunburst-graph', 'figure'), Input('drug4-sunburst-dropdown', 'value'))
def update_figure(selected_label):
    selected_column = demographic_column_map[selected_label]['column']
    selected_map = demographic_column_map[selected_label]['map']

    df_new = pd.concat([dataframe_demographic[selected_column], dataframe_drug], axis=1)

    df_grouped = df_new.groupby(selected_column).sum().stack().reset_index()
    df_grouped[selected_column] = df_grouped[selected_column].map(selected_map)
    df_final = df_grouped.rename(columns={'level_1': 'Drug', 0: 'Count'})

    fig = px.sunburst(
        df_final,
        path=['Drug', selected_column],
        values='Count',
        title=f"Division of {selected_label} groups for the top 4 drugs",
        width=500, 
        height=500
    )
    fig.update_layout(
        font=dict(
            family="PT Sans Narrow",
            size=11,
            color="RebeccaPurple"
        )
    )

    return fig


def generate_route_demographic_horizontal_bar():
    dropdown_labels = list(demographic_column_map.keys())

    return html.Div(children=[
        html.Label('Select one'),
        dcc.Dropdown(dropdown_labels, dropdown_labels[0], id='route-bar-dropdown', clearable=False),
        dcc.Graph(id='route-bar-graph')
    ])

@dash.callback(Output('route-bar-graph', 'figure'), Input('route-bar-dropdown', 'value'))
def update_figure(selected_label):
    selected_column = demographic_column_map[selected_label]['column']
    selected_map = demographic_column_map[selected_label]['map']

    df_new = pd.concat([dataframe_demographic[selected_column], dataframe_route], axis=1)

    df_grouped = df_new.groupby(selected_column).sum().stack().reset_index()
    df_grouped[selected_column] = df_grouped[selected_column].map(selected_map)
    df_final = df_grouped.rename(columns={'level_1': 'Route', 0: 'Count'})

    fig = px.bar(
        df_final,
        x='Count',
        y=selected_column,
        color='Route',
        orientation='h',
        barmode='group',
        title=f"Number of cases in each drug administration type\n grouped by demographic groups",
        width=500, 
        height=500,
        labels={"Count":"Number of cases", selected_column: selected_label}
    )
    fig.update_layout(
        font=dict(
            family="PT Sans Narrow",
            size=11,
            color="RebeccaPurple"
        )
    )

    return fig