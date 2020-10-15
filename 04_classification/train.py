import plotly.graph_objects as go
import plotly.offline as po
from plotly.subplots import make_subplots
from datetime import datetime
import pandas as pd
import argparse
import pickle
import os

# suppress logs
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = 3

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
# from arch import models

print(f'Tensorflow version: {tf.__version__}')