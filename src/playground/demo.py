import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("data/raw/titanic.csv")

df["age"] = pd.to_numeric(df["age"])


fig, ax1 = plt.subplots()
ax1.set_ylabel("")
ax1.set_xlabel("")
ax1.set_title("")
ax1.plot(df["age"])
ax1.grid()
plt.show(block=False)

df["fare"] = pd.to_numeric(df["fare"])
<<<<<<< HEAD




=======
>>>>>>> 4cac8cef251266b53fb947cef559bdce1f7470d5


