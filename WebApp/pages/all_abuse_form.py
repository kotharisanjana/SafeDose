import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from . import all_maps
from .generate_input import generate_input
from .pipeline import pipeline
import pandas as pd

df_cat_sdled_mapping = pd.read_csv('assets/cat_sdled_mapping.csv')

output_map = {
    'ALCOHOL': 'Alchohol',
    'NONALCILL': 'Illicit drugs (excluding alcohol)',
    'PHARMA': 'Pharmaceutical drugs',
    'NONMEDPHARMA': 'Pharmaceutical drugs used non-medically',
    'ALLABUSE': 'All misuse and abuse'
}

row1_inputs = [generate_input(column=column, input_row=1) for column in list(all_maps.ALL_ABUSE_INPUT_ROW_1.keys())]
row2_inputs = [generate_input(column=column, input_row=2) for column in list(all_maps.ALL_ABUSE_INPUT_ROW_2.keys())]
row3_inputs = [generate_input(column=column, input_row=3) for column in list(all_maps.ALL_ABUSE_INPUT_ROW_3.keys())]
row4_inputs = [generate_input(column=column, input_row=4) for column in list(all_maps.ALL_ABUSE_INPUT_ROW_4.keys())]
row5_inputs = [generate_input(column=column, input_row=5) for column in list(all_maps.ALL_ABUSE_INPUT_ROW_5.keys())]

all_inputs = html.Div(children=[
    html.Div(children=[
        html.H4('Demographic information'),
        dbc.Row(row1_inputs, className="input-row-values")
    ], className='input-row'),
    html.Div(children=[
        html.H4('Case information'),
        dbc.Row(row2_inputs, className="input-row-values")
    ], className='input-row'),
    html.Div(children=[
        html.H4('Drug 1 information'),
        dbc.Row(row3_inputs, className="input-row-values")
    ], className='input-row'),
    html.Div(children=[
        html.H4('Drug 2 information'),
        dbc.Row(row4_inputs, className="input-row-values")
    ], className='input-row'),
    html.Div(children=[
        html.H4('Drug 3 information'),
        dbc.Row(row5_inputs, className="input-row-values")
    ], className='input-row'),   
])

def generate_all_abuse_prediction():
    form = dbc.Form(all_inputs, className="abuse-form")
    return html.Div(children=[
        form,
        html.Div(
            children=[dbc.Button("Generate Abuse Indicators", id="open-modal", n_clicks=0)],
            className='generate-button'
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Generated Indicators")),
                dbc.ModalBody(id="modal-content", children=["Output Stuff"]),
                dbc.ModalFooter(dbc.Button("Close", id="close-modal", className="ms-auto", n_clicks=0))
            ], id="output-modal", is_open=False, backdrop="static", centered=True
        )
    ], className='predict-content-section')


@dash.callback(
    [Output("output-modal", "is_open"), Output("modal-content", "children")],
    [
        Input("open-modal", "n_clicks"), Input("close-modal", "n_clicks"),
        Input('METRO', 'value'), Input('AGECAT', 'value'), Input('SEX', 'value'), Input('RACE', 'value'),
        Input('CASETYPE', 'value'),
        Input('DRUGID_1', 'value'), Input('ROUTE_1', 'value'), Input('TOXTEST_1', 'value'),
        Input('DRUGID_2', 'value'), Input('ROUTE_2', 'value'), Input('TOXTEST_2', 'value'),
        Input('DRUGID_3', 'value'), Input('ROUTE_3', 'value'), Input('TOXTEST_3', 'value'),
    ],
    [State("output-modal", "is_open")]
)
def toggle_modal(
    open_clicks, close_clicks, 
    metro, age, sex, race, casetype,
    drug1, route1, tox1, drug2, route2, tox2, drug3, route3, tox3, 
    is_open
):
    def get_key_for_value(map, val):
        return [key for key, value in map.items() if value==val][0]

    metro_value = get_key_for_value(all_maps.METRO_map, metro)
    age_value = get_key_for_value(all_maps.AGECAT_map, age)
    sex_value = get_key_for_value(all_maps.SEX_map, sex)
    race_value = get_key_for_value(all_maps.RACE_map, race)

    casetype_value = get_key_for_value(all_maps.CASETYPE_map, casetype)

    drug1_value = get_key_for_value(all_maps.DRUGID_1_map, drug1)
    route1_value = get_key_for_value(all_maps.ROUTE_map, route1)
    tox1_value = get_key_for_value(all_maps.TOXTEST_map, tox1)

    drug2_value = get_key_for_value(all_maps.DRUGID_2_map, drug2)
    route2_value = get_key_for_value(all_maps.ROUTE_map, route2)
    tox2_value = get_key_for_value(all_maps.TOXTEST_map, tox2)

    drug3_value = get_key_for_value(all_maps.DRUGID_3_map, drug3)
    route3_value = get_key_for_value(all_maps.ROUTE_map, route3)
    tox3_value = get_key_for_value(all_maps.TOXTEST_map, tox3)

    data_to_add = {
        'DRUGID_1': [drug1_value],
        'ROUTE_1': [route1_value],
        'TOXTEST_1': [tox1_value],
        'DRUGID_2': [drug2_value],
        'ROUTE_2': [route2_value],
        'TOXTEST_2': [tox2_value],
        'DRUGID_3': [drug3_value],
        'ROUTE_3': [route3_value],
        'TOXTEST_3': [tox3_value],
        'CASETYPE': [casetype_value],
        'METRO': [metro_value],
        'AGECAT': [age_value],
        'SEX': [sex_value],
        'RACE': [race_value]
    }

    df_test = pd.DataFrame.from_dict(data_to_add)
    for index, drug in enumerate([drug1_value, drug2_value, drug3_value]):
        drug_row = df_cat_sdled_mapping[
            df_cat_sdled_mapping.eq(drug).any(axis=1)
        ].reset_index().drop(columns=['index', 'Unnamed: 0', 'DRUGID'])

        drug_row.columns = [f'{c}_{index+1}' for c in drug_row.columns]

        df_test = pd.concat([df_test, drug_row], axis=1)

    result_dict = pipeline(df_test)

    yes_abuse = [k for k,v in result_dict.items() if v==1]
    no_abuse = [k for k,v in result_dict.items() if v==0]

    yes_abuse_mapped = list(map(output_map.get, yes_abuse))
    no_abuse_mapped = list(map(output_map.get, no_abuse))

    yes_abuse_item_list = []
    no_abuse_item_list = []

    for abuse in yes_abuse_mapped:
        yes_abuse_item_list.append(html.Li(f'{abuse}'))
    for abuse in no_abuse_mapped:
        no_abuse_item_list.append(html.Li(f'{abuse}'))

    output_modal_content = html.Div(children=[
            html.H4('Catgories of substances abused:'),
            html.Ul(
                yes_abuse_item_list           
            ),
            html.H4('Catgories of substances NOT abused:'),
            html.Ul(
                no_abuse_item_list           
            )
    ])

    if open_clicks or close_clicks:
        return not is_open, [
           output_modal_content
        ]
    return is_open, [
        output_modal_content
        ]