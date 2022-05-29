import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns


model = keras.models.load_model('models\monster_generator.h5')


def create_prediction_array(level,size,environment,type,alignment,difficulty):
    '''
    inputs are from the app. These inputs will "turn on" on of the one-hot encoded columns in the case of environment, type, alignment. For challenge rating it will take the party level and add the difficulty factor
    size is a ordinal category from 1-6.

    All of these will be concatinated to form the final prediction array. 
    '''
    environ[environment] = 1
    m_type[type] = 1
    m_alignment[alignment] = 1
    challenge_r = level + difficulty
    cs_array = [challenge_r,size]

    final_array = np.concatenate((cs_array,environ,m_type,m_alignment))
    return final_array




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

