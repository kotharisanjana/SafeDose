import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/bias")

data = {'Before_classification': [14841, 88096, 9033, 18146, 793, 7421, 3253, 87628], 'After_classification_count': [42144, 6563, 13380, 6730, 12038, 0, 2793, -87628]}
casetype = ['Seeking Detox', 'Adverse Reaction', 'Suicide Attempt', 'Overmedication', 'Malicious Poisoning', 'Alcohol Only(Age<21)', 'Accidental Injestion', 'Other']

def make_casetype_bar():
    df_casetype = pd.DataFrame(data=data, index=casetype)
    df_casetype['After_classification'] = df_casetype\
        .apply(lambda x: x['Before_classification']+x['After_classification_count'], axis=1)
    df_final = df_casetype[['Before_classification', 'After_classification']]\
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

visuaization_row = html.Div(children=[html.Div(children=[
    html.Div(
        html.Img(
            src='/assets/confusion_matrix.png',
            className="class-report-image"
        )
    ),
    html.Div(
        html.Img(
            src='/assets/casetype_classification_report.jpeg',
            className="class-report-image"
        )
    )
    ], className='visualization-row'),
    html.Div(children=[
        html.Div(
            dcc.Graph(id='bias-casetype-count', figure=make_casetype_bar())
        ),
    ], className='visualization-row')
        
])

layout = html.Div(children=[
    why_row,
    solution_row,
    visuaization_row
], className="casetype-content-section")