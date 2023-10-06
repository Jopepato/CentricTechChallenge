"""Test for the config functions."""
from centric.conf import load_dataset_conf


def test_load_dataset_conf():
    """Test for the function load_dataset_conf."""
    dataset_conf = load_dataset_conf()
    assert "classes" in dataset_conf.keys()
