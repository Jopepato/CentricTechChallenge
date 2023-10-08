"""Functions realted to ETL and dataset processing."""
import numpy as np
from centric.constants import CLASS_GROUP
import tensorflow as tf
from tensorflow.keras import layers


def group_labels(y_labels: np.array) -> np.array:
    """
    Group the several classes into the same one to reduce the number of classes in our problem.

    Based on the description of the problem we want to group some of the classes together, as follows:
        0 - Upper part: T-shirt/top + Pullover + Coat + Shirt
        1 - Bottom part: Trouser
        2 - One piece: Dress
        3 - Footwear: Sandal + Sneaker + Ankle boot
        4 - Bags: Bag
    If we want to change this configuration in the future we can go to the constants file. A better way would be to store this
    in a configuration file that could be loaded.
    To simplify this problem we are going to assume that all the instances in the dataset come with a class that can be
    converted, if not we would need to add further checks to this function and think what to do with the classes that can
    not be grouped.

    :param
        y_labels: Numpy array with the original labels

    :return
        Numpy array with the same shape but with the classes grouped together
    """
    y_labels_grouped = np.vectorize(CLASS_GROUP.get)(y_labels)
    return y_labels_grouped


def rescale_data(data: np.array) -> np.array:
    """
    Preprocess the data to rescale to any dimensions and to divide it by 255, ready for the model.

    :param data:
        Numpy array with all the instances of the images
    :return:
        Images instances rescaled.
    """
    rescale = tf.keras.Sequential([layers.Rescaling(1.0 / 255)])

    data_rescaled = rescale(data)
    return data_rescaled
