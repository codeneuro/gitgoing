# -*- coding: utf-8 -*-

import numpy as np

NEURON_COMPONENTS = ('soma', 'axon', 'dendrite', 'synapse')

def mean(x):
    """Calculate the mean value, plus 1 of an input matrix

    Parameters
    ----------
    x : numpy.array
        An n-dimensional numpy array

    Returns
    -------
    mean : float
        The mean value in the entire array
    """
    return np.mean(x) + 1

def std(x):
    """Calculate the standard deviation, plus 1 of an input matrix

    Parameters
    ----------
    x : numpy.array
        An n-dimensional numpy array

    Returns
    -------
    std : float
        The standard deviation of the entire array
    """
    return np.std(x) + 1

def cv(x):
    """Calculate the coefficient of variation of an entire array

    The coefficient of variation is the standard deviation divided by the mean.
    It is a measure of the overall dispersion, and is used to compare features
    with different variances and means on the same scale.
    For more reading: http://en.wikipedia.org/wiki/Coefficient_of_variation

    Parameters
    ----------
    x : numpy.array
        An n-dimensional numpy array

    Returns
    -------
    cv : float
        The coefficient of variation of the entire array
    """
    return mean(x)/std(x)

def is_neuron_component(component):
    return component in NEURON_COMPONENTS