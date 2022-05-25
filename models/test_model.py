import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns


model = keras.models.load_model('models\monster_generator.h5')

environ = [0,0,0,0,0,0,0,0,0,0,0,0]
type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

environ[3] = 1
type[5] =1
alignment[1] = 1
challenge_r = [12 + 5]
size_r= [6]
final_array = np.concatenate((challenge_r,size_r,environ,type,alignment))

x_test = np.array([[17,  6,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]])

normalize(x_test)


test = model.predict(x_test)
test
