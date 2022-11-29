import dash
from dash import html, dcc

dash.register_page(__name__, path="/bias")

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

layout = html.Div(children=[
    why_row,
    solution_row
], className="casetype-content-section")