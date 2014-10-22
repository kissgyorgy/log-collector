from moving_average import moving_average
import pytest


def test_zeroes_only():
    assert moving_average([0, 0, 0], 2) == [0, 0]


def test_simple_dataset():
    assert moving_average([0, 1, 2], 2) == [0.5, 1.5]
