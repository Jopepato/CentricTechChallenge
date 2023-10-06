"""Functions realted to ETL and dataset processing."""
import numpy as np
from centric.conf import load_dataset_conf


def group_labels(y_labels: np.array) -> np.array:
    """
    Group the several classes into the same one to reduce the number of classes in our problem.

    Based on the description of the problem we want to group some of the classes together, as follows:
        0 - Upper part: T-shirt/top + Pullover + Coat + Shirt
        1 - Bottom part: Trouser
        2 - One piece: Dress
        3 - Footwear: Sandal + Sneaker + Ankle boot
        4 - Bags: Bag
    If we want to change this configuration in the future we can go to `conf/dataset.toml`
    To simplify this problem we are going to assume that all the instances in the dataset come with a class that can be
    converted, if not we would need to add further checks to this function and think what to do with the classes that can
    not be grouped.

    :param
        y_labels: Numpy array with the original labels

    :return
        Numpy array with the same shape but with the classes grouped together
    """
    classes_conf = load_dataset_conf()["classes"]
    classes_conf = {int(k): int(v) for k, v in classes_conf.items()}
    y_labels_grouped = np.vectorize(classes_conf.get)(y_labels)
    return y_labels_grouped
