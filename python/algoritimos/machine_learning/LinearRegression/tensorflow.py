import tensorflow as tf
import numpy
import pandas as pd
import matplotlib.pyplot as plt

rng = numpy.random

df = pd.read_csv("train.csv")

x = df["x"].values
y = df["y"].values