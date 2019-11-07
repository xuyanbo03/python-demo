#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/HR-all.csv')
print(df.head())
# 看连续值的直方图分布
sl_s = df['satisfaction_level']
sns.barplot(list(range(len(sl_s))),sl_s.sort_values())
plt.show()