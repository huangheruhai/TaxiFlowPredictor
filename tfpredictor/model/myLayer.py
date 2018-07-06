#!/usr/bin/env python
#-*- coding: utf-8 -*-

from keras.engine.topology import Layer
import keras.initializers as init

class myLayer(Layer):
        def __init__(self, **kwargs):
            super(myLayer, self).__init__(**kwargs)

        def build(self, input_shape):
            self.W = self.add_weight(name='kernel', shape=(input_shape[1:]), initializer=init.RandomUniform(0, 1),
                                          trainable=True)
            super(myLayer, self).build(input_shape)


        def call(self, x):
            return x * self.W



