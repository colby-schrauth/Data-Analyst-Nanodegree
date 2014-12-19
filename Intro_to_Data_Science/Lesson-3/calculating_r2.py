import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    data_avg = np.mean(data)
    cod_partone = np.sum((data - predictions)**2)
    cod_parttwo = np.sum((data - data_avg)**2)
    r_squared = 1 - (cod_partone / cod_parttwo)
    return r_squared
