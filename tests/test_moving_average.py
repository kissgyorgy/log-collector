from logcollector.moving_average import moving_average
import pytest


def test_zeroes_only():
    assert moving_average([0, 0, 0], 2) == [0, 0]


def test_simple_dataset():
    assert moving_average([0, 1, 2], 2) == [0.5, 1.5]


def test_complicated_dataset():
    dataset = [0.54, 0.21, 0.71, 0.17, 0.94, 0.7, 0.67, 1.0, 0.75, 0.63]
    results = [0.48667, 0.36333, 0.60667, 0.60333, 0.77, 0.79, 0.80667, 0.79333]
    assert moving_average(dataset, 3) == results
