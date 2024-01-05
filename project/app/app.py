
import numpy as np
import tensorflow as tf
from keras.models import load_model
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
   external_stylesheets=[dbc.themes.DARKLY],
)

server = app.server

app.title = "DnD Monster Generator"

model = load_model('monster_generator.h5')

#empty one-hot encoded arrays for the prediction

dataframe_columns = ['Hit Points','Armor Class','Proficiency Bonus','STR','DEX','CON','WIS','INT','CHA', 'STR_SV','DEX_SV','CON_SV','WIS_SV','INT_SV','CHA_SV', 'Attack_Bonus','Average_Damage_per_Round','Legendary Actions', 'Damage Resistances', 'Damage Immunities', 'Condition Immunities', 'Damage Vulnerabilities', 'Legendary Resistance', 'Magic Resistance']



def create_prediction_array(level,size,environment,type,alignment,difficulty):
    '''
    inputs are from the app. These inputs will "turn on" on of the one-hot encoded columns in the case of environment, type, alignment. For challenge rating it will take the party level and add the difficulty factor
    size is a ordinal category from 1-6.

    All of these will be concatinated to form the final prediction array. 
    '''
    environ = [0,0,0,0,0,0,0,0,0,0,0,0]
    m_type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m_alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    environ[environment] = 1
    m_type[type] = 1
    m_alignment[alignment] = 1
    challenge_r = level + difficulty
    cs_array = [challenge_r,size]

    final_array = np.concatenate((cs_array,environ,m_type,m_alignment))
   
    return  np.reshape(final_array,(1,44))

def prediction(array):
    pred = model.predict(array)

    # create dataframe from predictions
    monster_df = pd.DataFrame(data = pred.astype(int),columns=dataframe_columns)      
    
    return monster_df

# build component parts
stats_graph = dcc.Graph(id ="stats_graph")
SV_graph = dcc.Graph(id ="SV_graph")
HP_gauge =  daq.Gauge(id = 'HP', showCurrentValue=True, label='Hit Points',
     max=750, min=0)
AC_gauge = daq.Gauge(id = 'AC', showCurrentValue=True, label='Armor Class',
     max=30, min=0)
AB_gauge = daq.Gauge(id = 'AB', showCurrentValue=True, label='Attack Bonus',
     max=25, min=0)
Attack_gauge = daq.Thermometer(id = 'AD',showCurrentValue=True, label='Average Damage per Turn',height = 300, theme='dark',max=250, min=0)
Legendary_Actions = daq.BooleanSwitch(id='leg_ac',disabled=True, label = 'Legendary Actions')
Legendary_Resist = daq.BooleanSwitch(id='leg_res',disabled=True, label = 'Legendary Resistance')
Magic_Resist = daq.BooleanSwitch(id='mag_res',disabled=True, label = 'Magic Resistance')




#generator questions for model
sidebar =  html.Div([
                html.H2("Monster Stat Block Generator", style={'textAlign': 'center','font-size': 30}),
                html.Hr(),
                html.Div([
                    html.H4('4-Player Party Level', style={'font-size': 20}),
                    dcc.Slider(1,20,1,value=10,id='level-slider'),
                    html.Br(),
                    html.H4('Monster Size', style={'font-size': 20}),
                    dcc.RadioItems(
                        id= 'size',
                       options=[
                           {'label': 'Tiny', 'value': 1},
                           {'label': 'Small', 'value': 2},
                           {'label': 'Medium', 'value': 3},
                           {'label': 'Large', 'value': 4},
                           {'label': 'Huge', 'value': 5},
                           {'label': 'Gargantuan', 'value': 6},
                       ], style={'padding': 5}, labelStyle = {'padding':5},inline = True,
                       value=3
                    ),
                    html.Br(),
                    html.H4('Environment', style={'font-size': 20}),
                    dcc.Dropdown(
                        id = 'environment',
                        value=0,
                        clearable=False,
                        searchable=False,
                        style={'color':'black'},
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
                    html.Br(),
                    html.H4('Monster Type', style={'font-size': 20}),
                    dcc.Dropdown(
                        id = 'type',
                        value=0,
                        clearable=False,
                        searchable=False,
                        style={'color':'black'},
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
                    html.Br(),
                    html.H4('Alignment', style={'font-size': 20}),
                    dcc.Dropdown(
                        id = "alignment",
                        value=0,
                        clearable=False,
                        searchable=False,
                        style={'color':'black'},
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
                    html.H4('Difficulty', style={'font-size': 20}),
                    dbc.RadioItems(
                        id='difficulty',style={'padding': 10},
                        options =[
                            {'label': "Easy", 'value': -5},
                            {'label': "Medium", 'value': 0},
                            {'label': "Hard", 'value': 5},
                            {'label': "Deadly", 'value': 10}
                        ],
                    value=0),
                html.Br(),
                ]),   
            ], style = {"padding":"2rem"})

#Graph portion
content = html.Div([                                   
                dbc.Row([
                    dbc.Col([stats_graph]),
                    dbc.Col([SV_graph]),
                         ]),
                dbc.Row([
                    dbc.Col([HP_gauge]),
                    dbc.Col([AC_gauge]),
                    dbc.Col([AB_gauge]),
                         ]),
            ])

sidebar_right = html.Div( [dbc.Row([Attack_gauge]),
                        html.Hr(),
                        html.H3("Monster Traits", style={'textAlign': 'center'}),
                        dbc.Row([
                                dbc.Col(
                               dbc.Table(html.Tbody([
                                html.Tr([html.Td(['Damage Resistance: ']), html.Td(id='dam_res')]),
                                html.Tr([html.Td(['Damage Immunities: ']), html.Td(id='dam_imm')]),
                                html.Tr([html.Td(["Damage Vulnerabilities: "]), html.Td(id='dam_vul')]),
                                html.Tr([html.Td(["Condition Immunities: "]), html.Td(id='cond_imm')])]),bordered=True, dark=True,hover=True,striped=True),width={"size": 6, "offset": 3}),
                                dbc.Col()],
                       ),
                        dbc.Row([
                            dbc.Col([Legendary_Actions]),
                            dbc.Col([Legendary_Resist]),
                            dbc.Col([Magic_Resist]),
                         ]),
                       ])

app.layout = html.Div([
                
                #Header row that includes title and help button column              
                dbc.Row([
                    dbc.Col(html.H1('Dungeons and Dragons',
                                    style={'textAlign': 'left',
                                           'font-size': 50}),
                            width={'size':10}),
                    dbc.Col(dbc.Button('Help', color='info',className='me-1'),
                    width={'size':2})
                ]),
                dbc.Row([
                    #Div surrounding both the graphs and sidebar 
                   dbc.Col(sidebar,width={'size':3}),
                   dbc.Col(daq.DarkThemeProvider(theme={'dark': True}, children=content),width={'size':6}),
                   dbc.Col(daq.DarkThemeProvider(theme={'dark': True,'primary':'#0D7AFB'}, children=sidebar_right)
                      ,
                        width={'size':3}
                       )                                    
                ]),
])

@app.callback(
            [Output(component_id='stats_graph', component_property='figure'),
             Output(component_id='SV_graph', component_property='figure'),
             Output(component_id='HP', component_property='value'),
             Output(component_id='AC', component_property='value'),
             Output(component_id='AD', component_property='value'),
             Output(component_id='AB', component_property='value'),
             Output(component_id='leg_ac', component_property='on'),
             Output(component_id='leg_res', component_property='on'),
             Output(component_id='mag_res', component_property='on'),
             Output(component_id='dam_res', component_property='children'),
             Output(component_id='dam_imm', component_property='children'),
             Output(component_id='dam_vul', component_property='children'),
             Output(component_id='cond_imm', component_property='children')],
                [Input(component_id="level-slider", component_property='value'),
                 Input(component_id='size', component_property='value'),
                 Input(component_id='environment', component_property='value'),
                 Input(component_id='type', component_property='value'),
                 Input(component_id='alignment', component_property='value'),
                 Input(component_id='difficulty', component_property='value')
                 ])
def get_graph(level,size,environment,type,alignment,difficulty):

    monster_df= prediction(
        create_prediction_array(level,size,environment,type,alignment,difficulty))

    df = pd.DataFrame(dict(r = list(monster_df.iloc[0].to_numpy()[3:9]),  
    theta = list(monster_df.columns[3:9])))

    df_sv = pd.DataFrame(dict(r = list(monster_df.iloc[0].to_numpy()[9:15]),  
    theta = list(monster_df.columns[9:15])))

    #Radar graph stats
    stats_graph = px.line_polar(df, r='r', theta='theta', line_close=True)
    stats_graph.update_traces(fill='toself')
    stats_graph.update_layout(
        template='plotly_dark',
        polar=dict(radialaxis=dict(visible=True,range=[0,30])),paper_bgcolor='rgba(0,0,0,0)',
        title = {
            'text': "Monster Stats",
            'y':1,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
            title_font_color = 'white',
            hovermode='x')

    #Radar graph for saving throws
    SV_graph = px.line_polar(df_sv, r='r', theta='theta', line_close=True)
    SV_graph.update_traces(fill='toself')
    SV_graph.update_layout(
        template='plotly_dark',
        polar=dict(radialaxis=dict(visible=True,range=[0,20])),     paper_bgcolor='rgba(0,0,0,0)', 
        title = {
            'text': "Saving Throws",
            'y':1,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        title_font_color = 'white')

    # stats
    hit_points = monster_df.loc[0,'Hit Points']
    armor_class = monster_df.loc[0,'Armor Class']
    avg_damage = monster_df.loc[0,'Average_Damage_per_Round']
    attack_bonus = monster_df.loc[0,'Attack_Bonus']

    #Check Marks
    if monster_df.loc[0,'Legendary Actions'] == 1:
        leg_actions = True
    else:
        leg_actions = False

    if monster_df.loc[0,'Legendary Resistance'] == 1:
        leg_resist = True
    else:
        leg_resist = False
    
    if monster_df.loc[0,'Magic Resistance'] == 1:
        mag_resist = True
    else:
        mag_resist = False
    #numbers
    dam_res = monster_df.loc[0,'Damage Resistances']
    dam_immun = monster_df.loc[0,'Damage Immunities']
    dam_vuln = monster_df.loc[0,'Damage Vulnerabilities']
    cond_immun = monster_df.loc[0,'Condition Immunities']  

    return stats_graph,SV_graph,hit_points,armor_class,avg_damage, attack_bonus, leg_actions, leg_resist, mag_resist, dam_res, dam_immun, dam_vuln, cond_immun

#if __name__ =='__main__':
#    app.run_server(debug=True)herokuherok