
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

# Read iris data.
df = pd.read_csv('notebooks/iris.csv')
df.head()


# In[3]:

# Plot sepal length against sepal width.
df.plot(x='sepal_length', y='sepal_width', kind='scatter', figsize=(8,8))


# In[4]:

# Choose a random point from the data set.
import random

random.seed()
pt = df.iloc[random.choice(df.index.tolist())]
pt['sepal_length']


# In[5]:

# Create a new dataframe that contains the distance of every point from our randomly chosen point
import math

def dist_from_pt(p):
    """Calculate the distance of a point to a randomly chosen point."""
    return math.sqrt(((pt.sepal_length - p.sepal_length) ** 2) + ((pt.sepal_width - p.sepal_width) ** 2))

df['dist_from_pt'] = df[['sepal_length', 'sepal_width']].apply(func=dist_from_pt, axis=1)
df.head()


# In[6]:

# Look at 10 nearest neighbors.
df_sorted = df.sort_values(by='dist_from_pt', ascending=True)
df_sorted[0:10]


# In[14]:

df_sorted['species'][0:10].value_counts().index[0]


# In[17]:

def knn(k):
    """knn returns the majority class for the k nearest neighbors."""
    return df_sorted['species'][0:k].value_counts().index[0]


# In[19]:

print(knn(50))
