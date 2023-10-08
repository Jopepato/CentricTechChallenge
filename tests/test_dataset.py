"""Tests for the dataset.py functions."""
import numpy as np
from centric.dataset import group_labels, rescale_data


def test_group_labels():
    """Test for the function group_labels."""
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    a_grouped = group_labels(a)
    assert np.array_equal(a_grouped, np.array([0, 1, 0, 2, 0, 3, 0, 3, 4, 3]))


def test_rescale_data(get_test_data):
    """Test for the function rescale_data."""
    resized_data = rescale_data(get_test_data)

    assert np.min(resized_data) == 0
    assert np.max(resized_data) == 1
