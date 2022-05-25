import time
import importlib

import dash
from dash import dcc
from dash import html
import numpy as np
from dash.dependencies import Input, Output, State
import tensorflow as tf
import keras
from keras.models import load_model

import dash_bootstrap_components as dbc

import utils.figures as figs





app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

model = keras.models.load_model('models\monster_generator.h5')


environ = [0,0,0,0,0,0,0,0,0,0,0,0]
type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


app.title = "DnD Monster Generator"
server = app.server

app.layout = html.Div(
    children=[
        # .container class is fixed, .container.scalable is scalable
        html.Div(
            className="banner",
            children=[
                # Change App Name here
                html.Div(
                    className="container scalable",
                    children=[
                        # Change App Name here
                        html.H2(
                            id="banner-title",
                            children=[
                                html.A(
                                    "DnD Monster Generator",
                                    style={
                                        "text-decoration": "none",
                                        "color": "inherit",
                                    },
                                )
                            ],
                        ),
                  ],
                )
            ],
        ),
        html.Div(
            id="body",
            className="container scalable",
            children=[
                html.Div(
                    id="app-container",
                    # className="row",
                    children=[
                        html.Div(
                            # className="three columns",
                            id="left-column",
                            children=[
                                dcc.Slider(1,20,1, value =10, id='level-slider'),
                                html.Div(id='slider-output-container')
                    ]),
                                                      ),
                            html.Div(
                            id="div-graphs",
                            children=dcc.Graph(
                                id="graph-plotly",
                                figure=dict(
                                    layout=dict(
                                        plot_bgcolor="#282b38", paper_bgcolor="#282b38"
                                    )
                                ),
                            ),
                        ),
                    ],
                )
            ],
        ),
    ]
)


@app.callback(
    Output('slider-output-container','children'),
    [Input("level-slider", "value")],
)


@app.callback(
    Output("div-graphs", "children"),
    [
        Input('level-slider', "value"),
        Input("slider-svm-parameter-degree", "value"),
        Input("slider-svm-parameter-C-coef", "value"),
        Input("slider-svm-parameter-C-power", "value"),

    ],
)
def update_stat_graph(
    kernel,
    degree,
    C_coef,
    C_power,
    gamma_coef,
    gamma_power,
    dataset,
    noise,
    shrinking,
    threshold,
    sample_size,
):
   


    return [
        html.Div(
            id="svm-graph-container",
            children=dcc.Loading(
                className="graph-wrapper",
                children=dcc.Graph(id="graph-sklearn-svm", figure=prediction_figure),
                style={"display": "none"},
            ),
        ),
        html.Div(
            id="graphs-container",
            children=[
                dcc.Loading(
                    className="graph-wrapper",
                    children=dcc.Graph(id="graph-line-roc-curve", figure=roc_figure),
                ),
                dcc.Loading(
                    className="graph-wrapper",
                    children=dcc.Graph(
                        id="graph-pie-confusion-matrix", figure=confusion_figure
                    ),
                ),
            ],
        ),
    ]


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True)