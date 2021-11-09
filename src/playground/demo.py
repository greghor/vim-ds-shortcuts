import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("data/raw/titanic.csv")


df["age"] = pd.to_numeric(df["age"])




