import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dataframe = pd.read_csv('assets/demographic_data.csv')

AGECAT_map = {0:'NA', 1:'<= 5', 2:'6-11',3:'12-17', 4:'18-20', 5:'21-24', 6:'25-29', 7:'30-34', 8:'35-44', 9:'45-54', 10:'55-64',11:'>= 65'}
SEX_map = {0:'NA', 1:'Male', 2:'Female'}
RACE_map = {0:'NA', 1:'White', 2:'Black/African American',3:'Any Hispanic/Latino', 4:'All Other'}
METRO_map = {0:'NA', 1:'MA-NH', 2:'NY-NJ-PA',3:'IL-IN-WI', 4:'MI', 5:'MN-WI', 6:'FL', 7:'FL', 8:'TX', 9:'CO', 10:'AZ',11:'CA', 12:'CA', 13:'WA', 14:'Other'}
CASETYPE_map = {0: 'NA', 1:'Suicide Attempt', 2:'Seeking Detox',3:'Alcohol Only(Age<21)', 4:'Adverse Reaction', 5:'Overmedication', 6:'Malicious Poisoning', 7:'Accidental Injestion', 8:'Other'}
DISPOSITION_map = {0:'NA', 1:'Discharged home', 2:'Released to police/Jail',3:'Referred to detox/Treatment', 4:'ICU/Critical care', 5:'Surgery', 6:'Chemical dependency/detox, Psychiatric unit', 7:'Other inpatient unit', 8:'Transferred', 9:'Left agaist medical advice', 10:'Died',11:'Other'}
ALCOHOL_map = {0:'Alcohol not mentioned', 1: 'Alcohol mentioned'}
NONALCILL_map = {0:'Episode doesn\'t involve illicit drugs', 1: 'Episode involves illicit drugs'}
PHARMA_map = {0:'Episode doesn\'t involve pharmaceuticals', 1: 'Episode involves pharmaceuticals'}
NONMEDPHARMA_map = {0:'Episode doesn\'t involve non-medical use of pharmaceuticals', 1: 'Episode involves non-medical use of pharmaceuticals'}
ALLABUSE_map = {0:'Not an All Misuse and Abuse episode', 1:'Is an All Misuse and Abuse episode'}

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

episode_column_map = {
    'Alcohol': {
        'column':'ALCOHOL',
        'map': ALCOHOL_map
    }, 
    'Illicit Drugs': {
        'column':'NONALCILL',
        'map': NONALCILL_map
    },    
    'Pharmaceuticals': {
        'column':'PHARMA',
        'map': PHARMA_map
    },    
    'Non-medical use of Pharmaceuticals': {
        'column':'NONMEDPHARMA',
        'map': NONMEDPHARMA_map
    },  
    'Instance of All Abuse and Misuse': {
        'column':'ALLABUSE',
        'map': ALLABUSE_map        
    }
}

def generate_disposition_bubble():
    dropdown_labels = list(demographic_column_map.keys())
    return html.Div(children=[
        html.Label('Select one'),
        dcc.Dropdown(dropdown_labels, dropdown_labels[0], id='disposition-bubble-dropdown', clearable=False),
        dcc.Graph(id='disposition-bubble-graph')
    ])

@dash.callback(Output('disposition-bubble-graph', 'figure'), Input('disposition-bubble-dropdown', 'value'))
def update_figure(selected_label):
    selected_column = demographic_column_map[selected_label]['column']
    selected_map = demographic_column_map[selected_label]['map'] 

    df_grouped = dataframe.groupby([selected_column, 'DISPOSITION']).agg(
        Count=pd.NamedAgg(column='DISPOSITION', aggfunc="count")
    )
    index_0 = df_grouped.index.get_level_values(0).map(selected_map)
    index_1 = df_grouped.index.get_level_values(1).map(DISPOSITION_map)
    df_grouped_mapped = df_grouped.set_index([index_0, index_1])
    df_grouped_final = df_grouped_mapped.reset_index()

    fig = px.scatter(
        df_grouped_final, 
        x=selected_column, 
        y="DISPOSITION", 
        size="Count", 
        size_max=60,
        title=f"Bubble chart of Disposition of a case across {selected_label} groups",
        width=750, 
        height=500,
        labels={selected_column:selected_label, "DISPOSITION":"Disposition"}
    )

    return fig


def generate_casetype_sunburst():
    dropdown_labels = list(demographic_column_map.keys())
    return html.Div(children=[
        html.Label('Select one'),
        dcc.Dropdown(dropdown_labels, dropdown_labels[0], id='casetype-sunburst-dropdown', clearable=False),
        dcc.Graph(id='casetype-sunburst-graph')
    ])

@dash.callback(Output('casetype-sunburst-graph', 'figure'), Input('casetype-sunburst-dropdown', 'value'))
def update_figure(selected_label):
    selected_column = demographic_column_map[selected_label]['column']
    selected_map = demographic_column_map[selected_label]['map']

    df_grouped = dataframe.groupby([selected_column, 'CASETYPE']).agg(
        Count=pd.NamedAgg(column='CASETYPE', aggfunc="count")
    )
    index_0 = df_grouped.index.get_level_values(0).map(selected_map)
    index_1 = df_grouped.index.get_level_values(1).map(CASETYPE_map)
    df_grouped_mapped = df_grouped.set_index([index_0, index_1])
    df_grouped_top = df_grouped_mapped['Count'].groupby(selected_column, group_keys=False).nlargest(3)
    df_grouped_final = df_grouped_top.reset_index()

    fig = px.sunburst(
        df_grouped_final,
        path=[selected_column, "CASETYPE"],
        values='Count',
        title=f"Top three types of cases (by frequency) under each {selected_label} group",
        width=600, 
        height=500
    )

    return fig



def generate_episode_demographic_stacked_bar():
    demographic_dropdown_labels = list(demographic_column_map.keys())
    episode_dropdown_labels = list(episode_column_map.keys())
    demographic_dropdown = dbc.Row([
        dbc.Col(html.Label('Demographic group')),
        dbc.Col(dcc.Dropdown(demographic_dropdown_labels, demographic_dropdown_labels[0], id='demographic-bar-dropdown', clearable=False))
    ], justify="start", className="g-0")
    episode_dropdown = dbc.Row([
        dbc.Col(html.Label('Type of episode')),
        dbc.Col(dcc.Dropdown(episode_dropdown_labels, episode_dropdown_labels[0], id='episode-bar-dropdown', clearable=False, optionHeight=50))
    ], justify="start", className="g-0")
    return html.Div(children=[
        dbc.Row([
            dbc.Col(demographic_dropdown),
            dbc.Col(episode_dropdown)
        ]),
        dcc.Graph(id='demographic-episode-stackedbar-graph')
    ])

@dash.callback(Output('demographic-episode-stackedbar-graph', 'figure'), Input('demographic-bar-dropdown', 'value'), Input('episode-bar-dropdown', 'value'))
def update_figure(demographic_label, episode_label):
    demographic_column = demographic_column_map[demographic_label]['column']
    demographic_map = demographic_column_map[demographic_label]['map'] 

    episode_column = episode_column_map[episode_label]['column']
    episode_map = episode_column_map[episode_label]['map'] 

    df_grouped = dataframe.groupby([demographic_column, episode_column]).agg(
        Count=pd.NamedAgg(column=episode_column, aggfunc="count")
    )
    index_0 = df_grouped.index.get_level_values(0).map(demographic_map)
    index_1 = df_grouped.index.get_level_values(1).map(episode_map)
    df_grouped_mapped = df_grouped.set_index([index_0, index_1])
    df_grouped_final = df_grouped_mapped.reset_index()

    fig = px.bar(
        df_grouped_final,
        x=demographic_column,
        y='Count',
        color=episode_column,
        title=f"Number of cases in each demographic group stacked by type of episode",
        width=700, 
        height=500,
        labels={demographic_column:demographic_label, "Count":"Number of cases"}
    )

    return fig