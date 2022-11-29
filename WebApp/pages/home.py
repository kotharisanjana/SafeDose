import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

home_title = html.Div(
    children=[
        html.H3(children="This will be the project catchphrase")
])
home_cloud = html.Img(
    src='/assets/drug_cloud.png',
    className="cloud-image"
)

info_row = html.Div(children=[
    home_title,
    home_cloud
], className="d-flex justify-content-around info-row")

dashboard_card = html.Div(children=[
    dbc.Card([
        dbc.CardImg(src='/assets/dashboard-pic.png'),
        dbc.CardBody([
            dbc.CardLink('Dashboard', href=dash.page_registry['pages.dashboard']['path'])
        ], className="card-link")
    ])
], className="card-box")

predict_card = html.Div(children=[
    dbc.Card([
        dbc.CardImg(src='/assets/predict-pic.png'),
        dbc.CardBody([
            dbc.CardLink('Predict', href=dash.page_registry['pages.predict']['path'])
        ], className="card-link")
    ])
], className="card-box")

information_card = html.Div(children=[
    dbc.Card([
        dbc.CardImg(src='/assets/bias-pic.jpg'),
        dbc.CardBody([
            dbc.CardLink('Solving subjectivity', href=dash.page_registry['pages.bias']['path'])
        ], className="card-link")
    ])
], className="card-box")

card_row = html.Div(children=[
    dashboard_card, predict_card, information_card
], className="d-flex justify-content-center")


layout = html.Div(children=[
    info_row,
    card_row
])