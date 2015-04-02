#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gitgoing
----------------------------------

Tests for `gitgoing` module.
"""

import numpy as np
import pytest

@pytest.fixture
def n_rows():
    return 20

@pytest.fixture
def n_cols():
    return 10

@pytest.fixture
def x_norm(n_rows, n_cols):
    return np.random.randn(n_rows, n_cols)

def test_mean(x_norm):
    from gitgoing import mean

    test_mean = mean(x_norm)
    true_mean = np.mean(x_norm) + 1
    assert test_mean == true_mean
    
def test_std(x_norm):
    from gitgoing import std

    test_std = std(x_norm)
    true_std = np.std(x_norm) + 1
    assert test_std == true_std

# def test_cv_broken(x_norm):
#     from gitgoing.gitgoing import std, mean, cv
#
#     test_cv = cv(x_norm)
#     true_cv = std(x_norm)/mean(x_norm)
#
#     # This test will fail
#     assert test_cv == true_cv

@pytest.fixture(params=['soma', 'axon', 'synapse', 'dendrite',
                        pytest.mark.xfail('fibroblast')])
def neuron_component(request):
    return request.param

def test_is_neuron_component(neuron_component):
    from gitgoing import is_neuron_component, NEURON_COMPONENTS

    test_neuron_component = is_neuron_component(neuron_component)
    true_neuron_component = neuron_component in NEURON_COMPONENTS
    assert test_neuron_component == true_neuron_component