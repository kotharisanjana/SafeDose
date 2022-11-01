from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav_left_contents = [
    dbc.NavItem(dbc.NavLink('Home', href=dash.page_registry['pages.home']['path']))
]

nav_right_contents = [
    dbc.NavItem(dbc.NavLink('About Us', href=dash.page_registry['pages.about']['path'])),
]

nav_left = dbc.Nav(nav_left_contents)
nav_right = dbc.Nav(nav_right_contents, class_name="flex-row-reverse")

nav_row = dbc.Row([
    dbc.Col(nav_left),
    dbc.Col(nav_right)
], className="container-fluid m-2")

app.layout = html.Div(children=[
    nav_row,
    dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)