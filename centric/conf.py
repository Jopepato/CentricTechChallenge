"""Functions related to the configuration of the project."""
from centric.constants import DATASET_CONF_PATH
from typing import Dict
import tomli


def load_dataset_conf() -> Dict:
    """
    Load the configuration for the dataset in the
    :return:
    """
    with open(DATASET_CONF_PATH, mode="rb") as fp:
        config = tomli.load(fp)

    return config
