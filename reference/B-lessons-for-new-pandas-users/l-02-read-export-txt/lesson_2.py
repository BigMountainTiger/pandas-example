#!/usr/bin/env python
# coding: utf-8

# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
# %matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# The inital set of baby names
names = ['Bob','Jessica','Mary','John','Mel']


# np.random.seed?
# random.randint?
# len?
# range?
# zip?


random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records
# random_names[:10]


# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]
# births[:10]


BabyDataSet = list(zip(random_names,births))
# print(BabyDataSet[:10])


df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df[:5]


location = 'temp-data/births1880.txt'

df.to_csv(location,index=False,header=False)
df = pd.read_csv(location, header=None, names=['Names','Births'])

import os
os.remove(location)

print(df.shape)
df.head(5)


df['Names'].unique()


print(df['Names'].describe())


# df.groupby?
name = df.groupby('Names')

df = name.sum()
df


Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)


df['Births'].max()


# Create graph
df['Births'].plot.bar()

print("The most popular name")
print(df.sort_values(by='Births', ascending=False))

