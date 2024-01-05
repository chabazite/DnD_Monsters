import dash
import dash_bootstrap_components as dbc
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


app.title = "DnD Monster Generator"
server = app.server

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
                            {'label': "Underdark", 'value': 9 },          
                            {'label': "Underwater", 'value': 10},
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
                            {'label': "Lawful Good", 'value': 9 },          
                            {'label': "Lawful Neutral", 'value': 10},
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


if __name__ =='__main__':
    app.run_server(debug=True)