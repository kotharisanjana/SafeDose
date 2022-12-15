import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from . import all_maps


def generate_input(column: str, input_row: int):
    map_dict = {}
    if input_row == 1:
        map_dict = all_maps.ALL_ABUSE_INPUT_ROW_1
    elif input_row == 2:
        map_dict = all_maps.ALL_ABUSE_INPUT_ROW_2
    elif input_row == 3:
        map_dict = all_maps.ALL_ABUSE_INPUT_ROW_3
    elif input_row == 4:
        map_dict = all_maps.ALL_ABUSE_INPUT_ROW_4
    else:
        map_dict = all_maps.ALL_ABUSE_INPUT_ROW_5

    # if column == 'CASEWGT':
    #     input_label = map_dict[column]['label']
    #     return dbc.Col(
    #         html.Div(children=[
    #             dbc.Label(input_label, html_for=input_label),
    #             dcc.Input(id=column, value=0.00, type='number')
    #         ]), className='input-col'
    #     )
    # else:
    input_label = map_dict[column]['label']
    dropdown_labels = list(map_dict[column]['map'].values())
    
    return dbc.Col(
        html.Div(children=[
            dbc.Label(input_label, html_for=input_label),
            dcc.Dropdown(dropdown_labels, dropdown_labels[0], id=column, clearable=False)
        ]), className='input-col'
    )