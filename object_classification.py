import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import pickle
import matplotlib.pyplot as plt
import numpy as np
(X_train, y_train), (X_test,y_test) = datasets.cifar10.load_data()
X_train.shape

y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)
classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
def plot_sample(X, y, index):
    plt.figure(figsize = (15,2))
    plt.imshow(X[index])
    plt.xlabel(classes[y[index]])
    plt.show()
# plot_sample(X_train, y_train, 0)


X_train = X_train / 255.0
X_test = X_test / 255.0


pickled_model = pickle.load(open('model.pkl', 'rb'))
y_pred = pickled_model.predict([tf.data.Dataset.from_tensor_slices()])
print(X_test[0].reshape(-1,1))
input_layer= layers.InputLayer(input_shape=(2,2,1))
conv1 = layers.Conv2D(3,(2,2))
X= np.ones((2,2))
X =X.reshape(1,X.shape[0],X.shape[1],1) # shape of X is 4D, (1, 2, 2, 1) 
conv1(input_layer(X))

