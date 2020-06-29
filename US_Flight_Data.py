
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[26]:


url = 'https://raw.githubusercontent.com/aliceblueberry/covid19_sura/master/flight%20data.csv'
df = pd.read_csv(url)
df = df.drop(df.columns[[1,2,3,4,5,8,9,10,13,14,15,16]], axis = 1)
df = df.loc[df['PASSENGERS']>0]
df = df.reset_index(drop = True)


# In[27]:


df = df.groupby(['ORIGIN_STATE_ABR', 'DEST_STATE_ABR']).sum()
df.to_csv('clean_flight.csv')


# In[49]:


plt.hist(df[df['PASSENGERS']<100000]['PASSENGERS'], bins = 100)


# In[16]:


def normalize(c):
    upper = c.max()
    lower = c.min()
    y = (c - lower)/(upper-lower)
    return y


# In[29]:


df_normalized = df.copy()
df_normalized['PASSENGERS'] = normalize(np.log(df_normalized['PASSENGERS']))
df_normalized.rename(columns={'PASSENGERS': 'PASSENGERS_NORMALIZED'})

