from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Model

from tensorflow.keras.saving import register_keras_serializable

@register_keras_serializable(package="Custom", name="mymodel")
class mymodel(Model):
  def __init__(self, **kwargs) -> None:
     super().__init__(**kwargs)

     self.conv1=Conv2D(32,(3,3),padding="same",activation="relu",input_shape=(150,150,1))
     self.maxpool1=MaxPooling2D((2,2))

     self.conv2=Conv2D(64,(3,3),padding="same",activation="relu")
     self.maxpool2=MaxPooling2D((2,2))

     self.conv3=Conv2D(128,(3,3),padding="same",activation="relu")
     self.maxpool3=MaxPooling2D((2,2))

     self.flatten=Flatten()
     self.dense1=Dense(128,activation="relu")
     self.dropout=Dropout(0.5)
     self.dense2=Dense(64,activation="relu")
     self.dense3=Dense(32,activation="relu")
     self.dense4=Dense(1,activation="sigmoid")

  def call(self,inputs):
    x=self.conv1(inputs)
    x=self.maxpool1(x)

    x=self.conv2(x)
    x=self.maxpool2(x)

    x=self.conv3(x)
    x=self.maxpool3(x)

    x=self.flatten(x)
    x=self.dense1(x)
    x=self.dropout(x)
    x=self.dense2(x)
    x=self.dense3(x)
    x=self.dense4(x)
    return x