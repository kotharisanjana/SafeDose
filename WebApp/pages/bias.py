import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/bias")

dataframe_demographic = pd.read_csv('assets/demographic_data.csv')
CASETYPE_map = {0: 'NA', 1:'Suicide Attempt', 2:'Seeking Detox',3:'Alcohol Only(Age<21)', 4:'Adverse Reaction', 5:'Overmedication', 6:'Malicious Poisoning', 7:'Accidental Injestion', 8:'Other'}
count_after_classification = {'Seeking Detox':42144, 'Adverse Reaction':6563, 'Suicide Attempt':13380, 'Overmedication':6730, 'Malicious Poisoning': 12038, 'Alcohol Only(Age<21)':0, 'Accidental Injestion': 2793, 'Other':-83648}

def make_casetype_bar():
    df_casetype_count_before = dataframe_demographic.groupby('CASETYPE').agg(
        Before_Classification=pd.NamedAgg(column='CASETYPE', aggfunc="count")
    )
    casetype_index = df_casetype_count_before.index.map(CASETYPE_map)
    df_casetype_count_before_mapped = df_casetype_count_before.set_index(casetype_index)

    df_casetype_count_after = pd.Series(data=count_after_classification, name='Count_After')   
    
    df_casetype_count = pd.concat([df_casetype_count_before_mapped, df_casetype_count_after], axis=1)
    df_casetype_count['After_Classification'] = df_casetype_count\
        .apply(lambda x: x['Before_Classification']+x['Count_After'], axis=1)
    df_final = df_casetype_count[['Before_Classification', 'After_Classification']]\
        .unstack()\
        .reset_index()\
        .rename(columns={'level_0':'Classification', 'level_1':'Casetype', 0: 'Count'})

    fig = px.bar(
        df_final,
        x='Casetype',
        y='Count',
        color='Classification',
        barmode='group',
        title=f"Number of cases before and after removing 'Other'",
        width=500, 
        height=500,
        labels={"Count":"Number of cases", "Casetype": "Case Type"}
    )
    fig.update_layout(
        font=dict(
            family="PT Sans Narrow",
            size=11,
            color="RebeccaPurple"
        )
    )

    return fig


why_row = html.Div(children=[
    html.Div("DAWN Reporters assign each visit to one of eight case types"),
    html.Ul([
        html.Li("Suicide Attempt"),
        html.Li("Seeking detoxification"),
        html.Li("Underage drinking"),
        html.Li("Adverse reaction"),
        html.Li("Over-medication"),
        html.Li("Malicious poisoning"),
        html.Li("Accidental ingestion"),
        html.Li("Other"),
    ]),
    html.Div("Most cases of drug abuse are classified as Other. This approach, which never directly identifies drug abuse, comes from the\
            recognition that medical records frequently lack explicit documentation of substance abuse.\
            This lack of documentation may occur for several reasons"),
    html.Ul([
        html.Li("First, the distinctions among use, misuse, and abuse are often subjective"),
        html.Li("Second, if there is a low index of suspicion for drug abuse in some types of patients \
            (e.g., older adults), ED physicians may be unlikely to label those types of patients as drug abusers"),
        html.Li("Third, ED staff may be concerned that the patient's insurance company will disallow \
            coverage if the visit is related to substance abuse"),
    ]),
], className="information-row")

solution_row = html.Div(children=[
    html.Div("We attempted to address this issue using Machine Learning by creating a supervised Classifier that learns from\
        the already labeled cases and annotates the 'Other' cases into one of the seven")
], className="information-row")

visuaization_row = html.Div(children=[
        html.Div(
            dcc.Graph(id='bias-casetype-count', figure=make_casetype_bar())
        ),
        html.Div(
            html.Img(
                src='/assets/casetype_classification_report.jpg',
                className="class-report-image"
            )
        )
    ], className='visualization-row')

layout = html.Div(children=[
    why_row,
    solution_row,
    visuaization_row
], className="casetype-content-section")