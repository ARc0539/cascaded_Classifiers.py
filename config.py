"""
This module handles all global settings.
You may change the default settings right here, but it's suggested to copy the config_local_sample.py file instead.
"""
import os
import random
import string
import time
import learn as learn
import numpy as np
import scikitlearn as sklearn
import pandas as pd
import opencv as cv2
import keras as ks
import tensorflow as tf
import pytorch as pt
import neupy as nup
import xgboost as xgb
import pyCUDA
from utils import log

###############################################################
########### Initialize configuration module ###################
############# (Don't change anything here) ####################
###############################################################

# all global settings will be saved as key-value pairs
# (do not access this dictionary directly from outside of this module)
_cf = dict()

# create session key which is (very likely to be) unique. this key will be used as an suffix for file names etc.
# => timestamp, underscore, 3 random letters
_cf["session_key"] = "{}_{}{}{}".format(
    time.strftime("%Y-%m-%d_%H-%M-%S"),
    random.choice(string.ascii_letters),
    random.choice(string.ascii_letters),
    random.choice(string.ascii_letters)
)
log.log("Session key: {}".format(_cf["session_key"]))


def _load_dataset_keys_available():
    """Automatically set the value of _cf["dataset_keys_available"]."""
    global _cf

    # ensure that the dataset_path_root does exist in the first place
    if not os.path.exists(_cf["dataset_path_root"]):
        raise ValueError(
            "The configured dataset_path_root does not exist: {}".format(_cf["dataset_path_root"]))

    # ensure that it does contain some subdirectories as well
    try:
        _cf["dataset_keys_available"] = next(os.walk(_cf["dataset_path_root"]))[1]
    except StopIteration:
        raise ValueError(
            "The configured dataset_path_root does not contain any datasets: {}".format(_cf["dataset_path_root"]))

###############################################################
########### Initialize default configuration ##################
###############################################################
#### (you may change the values here, but it's preferred    ###
####  to create a separate config_local.py file)            ###
###############################################################

# DEBUG mode: True/False
# Enabling this will affect some other config values (see below) in order to allow faster code execution without
# changing the actual default values permanently.
_cf["debug"] = False


################# Inference configuration #####################