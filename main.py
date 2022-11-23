import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input , Output

df =pd.read_csv('Covid19VacunasAgrupadas.csv')

app = dash.Dash(__name__)
app.layout= html.Div([
    html.Div([
        html.H1('Vacunados por Covid'),
        html.Img(src='assets/vacuna.png')
    ], className='banner'),

    html.Div([
        html.Div([
            html.P('selecciona la dosis', className='fix_label', style={'color':'black', 'margin-top':'2px'}),
            dcc.RadioItems(id='dosis-raddio-item',
                            labelStyle= {'display':'inline-block'},
                            options=[
                                {'label': 'primera dosis', 'value': 'primera_dosis_cantidad'},
                                {'label': 'segunda dosis', 'value': 'dosis_unica_cantidad'}

                            ],value = 'primera_dosis_cantidad', 
                            style= {'text-align':'center','color':'black'},className='dcc_compon')
        ],className='create_container2', style={'margin-bottom': '20px'})
    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='my-graph', figure={})
        ],className= ' create_container2'),

        html.Div([
            dcc.Graph(id='pie_graph', figure={})
        ],className='create_container2'),
    ])
])

@app.callback(
    Output('my-graph', component_property='figure'),
    Input('dosis-raddio-item', component_property='value'))

def update_graph(value):
    if value == 'primera_dosis_cantidad':
        fig= px.bar(
            data_frame=df,
            x= 'jurisdiccion_nombre',
            y= 'primera_dosis_cantidad'
        )
    else:
           fig= px.bar(
            data_frame=df,
            x= 'jurisdiccion_nombre',
            y= 'segunda_dosis_cantidad'
        )
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    Input('dosis-raddio-item', component_property='value'))

def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig2= px.pie(
            data_frame= df,
            names= 'jurisdiccion_nombre',
            values= 'primera_dosis_cantidad'
        )
    else:
         fig2= px.pie(
            data_frame= df,
            names= 'jurisdiccion_nombre',
            values= 'segunda_dosis_cantidad'
        )
    return fig2



if __name__=='__main__':
    app.run_server(debug=True)