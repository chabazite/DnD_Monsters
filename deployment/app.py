import numpy as np
import tensorflow as tf
import keras
from keras.models import load_model
#import the required libraries
import dash
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
import dash_daq as daq
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc




app = dash.Dash(
    __name__,
   external_stylesheets=[dbc.themes.SOLAR],
)

model = keras.models.load_model('models\monster_generator.h5')

#empty one-hot encoded arrays for the prediction
environ = [0,0,0,0,0,0,0,0,0,0,0,0]
type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dataframe_columns = ['Hit Points','Armor Class','Proficiency Bonus','STR','DEX','CON','WIS','INT','CHA', 'STR_SV','DEX_SV','CON_SV','WIS_SV','INT_SV','CHA_SV', 'Attack_Bonus','Average_Damage_per_Round','Legendary Actions', 'Damage Resistances', 'Damage Immunities', 'Condition Immunities', 'Damage Vulnerabilities', 'Legendary Resistance', 'Magic Resistance']



def create_prediction_array(level,size,environment,type,alignment,difficulty):
    '''
    inputs are from the app. These inputs will "turn on" on of the one-hot encoded columns in the case of environment, type, alignment. For challenge rating it will take the party level and add the difficulty factor
    size is a ordinal category from 1-6.

    All of these will be concatinated to form the final prediction array. 
    '''
    environ[environment] = 1
    type[type] =1
    alignment[alignment] = 1
    challenge_r = [level + difficulty]
    size_r= [size]
    final_array = np.concatenate((challenge_r,size_r,environ,type,alignment))
    return final_array

def prediction(array):
    pred = model.predict(array)

    # create dataframe from predictions
    monster_df = pd.DataFrame(data = pred,columns=dataframe_columns)      
    
    return monster_df

# build component parts
stats_graph = dcc.Graph(id ="stats_graph", style ={"height":"500px"})
SV_graph = dcc.Graph(id ="SV_graph", style ={"height":"500px"})
HP_gauge =  daq.Gauge(showCurrentValue=True, value=400, label='Hit Points',
     max=1000, min=0)
AC_gauge = daq.Gauge(showCurrentValue=True, value=15, label='Armor Class',
     max=30, min=0)
Attack_gauge = daq.Gauge(showCurrentValue=True, value=150, label='Average Damage per Turn',
     max=300, min=0)


app.title = "DnD Monster Generator"
server = app.server

#generator questions for model
sidebar =  html.Div([
                html.H2("DnD Monster Generator", style={'textAlign': 'center',
                                           'font-size': 30}),
                html.Hr(),
                html.Div([
                    html.Label('4-Player Party Level'),
                    dcc.Slider(1,20,1,value=10,id='level-slider'),
                    html.Label('Monster Size'),
                    dcc.RadioItems(
                        id= 'size',
                       options=[
                           {'label': 'Tiny', 'value': 1},
                           {'label': 'Small', 'value': 2},
                           {'label': 'Medium', 'value': 3},
                           {'label': 'Large', 'value': 4},
                           {'label': 'Huge', 'value': 5},
                           {'label': 'Gargantuan', 'value': 6},
                       ],
                       value=3
                    ),
                    html.Label('Environment'),
                    dcc.Dropdown(
                        id = 'environment',
                        options=[
                            {'label': "Arctic", 'value': 0},
                            {'label': "Coastal", 'value': 1},
                            {'label': "Desert", 'value': 2},
                            {'label': "Forest", 'value':3},
                            {'label': "Grassland", 'value': 4},
                            {'label': "Hill", 'value': 5},
                            {'label': "Mountain", 'value': 6},
                            {'label': "NA", 'value': 7},        
                            {'label': "Swamp", 'value': 8},
                            {'label': "Underdark", 'value': 9 },          {'label': "Underwater", 'value': 10},
                            {'label': "Urban", 'value': 11},]
                    ),
                    html.Label('Monster Type'),
                    dcc.Dropdown(
                        id = 'type',
                        options=[
                            {'label': "Beast", 'value': 0},
                            {'label': "Dragon", 'value': 1},
                            {'label': "Humanoid", 'value': 2},
                            {'label': "Monstrosity", 'value':3},
                            {'label': "Fiend", 'value': 4},
                            {'label': "Undead", 'value': 5},
                            {'label': "Elemental", 'value': 6},
                            {'label': "Construct", 'value': 7},        
                            {'label': "Swarm", 'value': 8},
                            {'label': "Giant", 'value': 9},
                            {'label': "Plant", 'value': 10},
                            {'label': "Abberation", 'value': 11},
                            {'label': "Fey", 'value': 12},
                            {'label': "Celestial", 'value': 13},
                            {'label': "Ooze", 'value': 14}
                            ]
                    ),
                    html.Label('Alignment'),
                    dcc.Dropdown(
                        id = "Alignment",
                        options=[
                            {'label': "Any Alignment", 'value': 0},
                            {'label': "Any Chaotic Alignment", 'value': 1},
                            {'label': "Any Evil Alignment", 'value': 2},
                            {'label': "Any Non-Good Alignment", 'value':3},
                            {'label': "Any Non-Lawful Alignment", 'value': 4},
                            {'label': "Chaotic Evil", 'value': 5},
                            {'label': "Chaotic Good", 'value': 6},
                            {'label': "Chaotic Neutral", 'value': 7},        
                            {'label': "Lawful Evil", 'value': 8},
                            {'label': "Lawful Good", 'value': 9 },          {'label': "Lawful Neutral", 'value': 10},
                            {'label': "True Neutral", 'value': 11},
                            {'label': "Neutral Evil", 'value': 12},
                            {'label': "Neutral Good", 'value': 13},
                            {'label': "Unaligned", 'value': 14}                          
                        ]
                    ),
                    html.Br(),
                    html.Label('Difficulty'),
                    dbc.RadioItems(
                        id='difficulty',
                        options =[
                            {'label': "Easy", 'value': -5},
                            {'label': "Medium", 'value': 0},
                            {'label': "Hard", 'value': 5},
                            {'label': "Deadly", 'value': 10}
                        ],
                    value=0),
                html.Br(),
                ]),   
            ])

#Graph portion
content = html.Div([                                   
                dbc.Row([
                    dbc.Col([stats_graph],md=2),
                    dbc.Col([SV_graph],md=2),
                         ]),
                dbc.Row([
                    dbc.Col([HP_gauge],md=3),
                    dbc.Col([AC_gauge],md=3),
                    dbc.Col([Attack_gauge],md=3),
                         ]),
            ])
app.layout = html.Div([
                #Header row that includes title and help button column              
                dbc.Row([
                    dbc.Col(html.H1('DnD Monster',
                                    style={'textAlign': 'left',
                                           'font-size': 50}),
                            width={'size':10}),
                    dbc.Col(dbc.Button('Help', color='info',className='me-1'),
                    width={'size':2})
                ]),
                #Tab Row that allows us to change from WQ to Equipment
                dbc.Row([
                    #Div surrounding both the graphs and sidebar filters
                   dbc.Col(sidebar,width={'size':3}),
                   dbc.Col(content,width={'size':9}),
                        #Sidebar filters                
                ]),
])

@app.callback(
            [Output(component_id='stats_graph', component_property='children'),
             Output(component_id='SV_graph', component_property='children')],
                [Input(component_id="level-slider", component_property='value'),
                 Input(component_id='size', component_property='value'),
                 Input(component_id='environment', component_property='value'),
                 Input(component_id='type', component_property='value'),
                 Input(component_id='alignment', component_property='value'),
                 Input(component_id='difficulty', component_property='value')
                 ])
def get_graph(level,size,environment,type,alignment,difficulty):

    monster_df= prediction(
        create_prediction_array(
            level,
            size,
            environment,
            type,
            alignment,
            difficulty))

    r = list(monster_df[3:9])
    theta = list(monster_df.columns[3:9])

    #Radar graph stats
    stats_graph = px.line_polar(monster_df, r=r, theta=theta, line_close=True)
    stats_graph.update_traces(fill='toself')

    #Radar graph for saving throws
    SV_graph = px.line_polar(monster_df, r=r, theta=theta, line_close=True)
    SV_graph.update_traces(fill='toself')
    return stats_graph,SV_graph

if __name__ =='__main__':
    app.run_server(debug=False)