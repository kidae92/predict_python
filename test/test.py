import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

# 총 126143개 데이터
path = '.\\data.csv'

df = pd.read_csv(path, encoding='cp949')

df.shape

uni_data = df['temperature']
uni_data.index = df['index']

uni_data.plot(subplots=True)

plt.show()