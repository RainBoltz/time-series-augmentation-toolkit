import numpy as np

def DN(ts, sigma=0.0, mu=1.0, alpha=1.0, random_seed=None):
'''
ts: np.array, time series data
sigma: float, standard deviation of the noise distribution
mu: float, mean of the noise distribution
alpha: float, the ratio of changes (new_value = alpha * delta + original_value)
random_seed: int, set numpy random seed
'''
    return ts

def WS(ts_set, n=None, random_seed=None):
'''
ts_set: np.ndarray, time series dataset
slicing_size: int, size of the sliced series, if None then default to 1/4 data length
random_seed: int, set numpy random seed
'''
    return ts_set

def WW(ts, n=None, alpha=0.5, random_seed=None):
'''
ts: np.array, time series data
n: int, influence range (+/-n values), if None then default to 1
alpha: float, the ratio of streching
random_seed: int, set numpy random seed
'''
    return ts

def DM(ts_set, random_seed=None):
'''
ts_set: np.ndarray, time series dataset

//TODO

random_seed: int, set numpy random seed
'''
    return ts_set