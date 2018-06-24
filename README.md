A project based on DeepST of @lucktroy
Rewrite and restructured with python3.6.3 , tensorflow 1.7.0 and keras 2.2

DeepST
======
[DeepST](https://github.com/lucktroy/DeepST): A **Deep Learning** Toolbox for Spatio-Temporal Data


## Installation

DeepST uses the following dependencies: 

* [Keras](https://keras.io/#installation) and its dependencies are required to use DeepST. Please read [Keras Configuration](keras_configuration.md) for the configuration setting. 
* [TensorFlow](https://github.com/tensorflow/tensorflow#download-and-setup)
* numpy and scipy
* HDF5 and [h5py](http://www.h5py.org/)
* [pandas](http://pandas.pydata.org/)
* CUDA 7.5 or latest version. And **cuDNN** is highly recommended. 


```

## Data path

The default `DATAPATH` variable is `DATAPATH=[path_to_DeepST]/data`. You may set your `DATAPATH` variable using

```

# Linux
export DATAPATH=[path_to_your_data]
```

## License

DeepST is released under the MIT License (refer to the LICENSE file for details).
