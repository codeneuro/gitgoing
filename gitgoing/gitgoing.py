# -*- coding: utf-8 -*-

import numpy as np

__all__ = ['mean_plus_one', 'std_plus_one', 'cv', 'is_neuron_component',
           'NEURON_COMPONENTS']


NEURON_COMPONENTS = ('soma', 'axon', 'dendrite', 'synapse')


def mean_plus_one(x):
    """Calculate the mean_plus_one value, plus 1 of an input matrix

    Parameters
    ----------
    x : numpy.array
        An n-dimensional numpy array

    Returns
    -------
    mean_plus_one : float
        The mean_plus_one value in the entire array
    """
    return np.mean(x) + 1

def std_plus_one(x):
    """Calculate the standard deviation, plus 1 of an input matrix

    Parameters
    ----------
    x : numpy.array
        An n-dimensional numpy array

    Returns
    -------
    std_plus_one : float
        The standard deviation of the entire array
    """
    return np.std(x) + 1

def cv(x):
    """Calculate the coefficient of variation of an entire array

    The coefficient of variation is the standard deviation divided by the
    mean_plus_one. It is a measure of the overall dispersion, and is used to
    compare features with different variances and means on the same scale.

    \mu/\sigma

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
    return mean_plus_one(x)/std_plus_one(x)

def is_neuron_component(component):
    return component in NEURON_COMPONENTS