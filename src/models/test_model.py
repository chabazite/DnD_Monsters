import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns


model = keras.models.load_model('..\..\models\monster_generator.h5')


def create_prediction_array(level,size,environment,type,alignment,difficulty):
    '''
    In the case of Environment, Type, and Alignment, one of the zeros in the lists created outside this function (examples below) will be exchanged for a one, based on the position number input. This translates to a feature column created through one-hot encoding.
    
    For challenge rating it will take the party level and add the difficulty factor
    
    Size is a ordinal category from 1-6.

    All of these will be concatinated to form the final prediction array.

    inputs:
            level: .25 - 30 based on input from app. 
            size: 1,2,3,4,5,6 based on input from the app
            environment: input from app. converted into position number for list below.
            type:input from app. converted into position number for list below.
            alignment:input from app. converted into position number for list below.
            difficulty: -5, 0, 5, 10 based on easy medium, hard, deadly input from app. 
    outputs:
            final_array: A combination of all inputs from the app the create a prediction input array to be placed into the monster generator model.

    '''
    environ[environment] = 1
    m_type[type] = 1
    m_alignment[alignment] = 1
    challenge_r = level + difficulty
    cs_array = [challenge_r,size]

    final_array = np.concatenate((cs_array,environ,m_type,m_alignment))
    return final_array



#Example lists used for testing purposes
environ = [0,0,0,0,0,0,0,0,0,0,0,0]
m_type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m_alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


y_test = create_prediction_array(17,6,3,8,5,0)

x_test = np.array([[17,  6,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]])


test = model.predict(y_test)
test

y_test = np.reshape(y_test,(1,44))

y_test.ndim
x_test.ndim

