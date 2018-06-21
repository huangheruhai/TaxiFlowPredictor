#!/usr/bin/env python
#-*- coding: utf-8 -*-
from keras import backend as K
from keras.engine.topology import Layer
import keras.initializers as init

class myLayer(Layer):
    def __init__(self,**kwargs):
        super(myLayer,self).__init__(**kwargs)

    def bulid(self,input_shape):
        self.kernel=self.add_weight(name='kernel',shape=(input_shape[1:]),initializer=init.RandomUniform(0,1),trainable=True)
        super(myLayer,self).build(input_shape)

    def call(self,x):
        return K.dot(x,self.kernel)

    # def compute_output_shape(self, input_shape):
    #     return (input_shape[0], input_shape[0])