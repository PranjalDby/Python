from statistics import mode
from unicodedata import name
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers;
# layer1 = layers.Dense(2,activation="relu",name="layer1");
# layer2 = layers.Dense(3,activation="relu",name="layer2");
# layer3=layers.Dense(4,name="layer3");

# x=tf.ones(3,3);
# y=layer3(layer2(layer1(x)))
# model.layers

#creating sequential model
# model=keras.Sequential(
#     [
#         layers.Dense(2,activation="relu"),
#         layers.Dense(3,activation="relu"),
#         layers.Dense(4),
#     ]
# )
# model=keras.Sequential(name="my_sequence")
# model.add(layers.Dense(2,activation="relu",name="layer1"))
# model.add(layers.Dense(3,activation="relu",name="layer2"))
# model.add(layers.Dense(4,activation="relu",name="layer3"))
# model.add(layers.Dense(5,name="layer4"))
# # model.pop()
# print(len(model.layers))
# # print(model.layers.name)

layer=layers.Dense(3)
layer.weights

x=tf.ones((1,4))
y=layer(x)
layer.weights


