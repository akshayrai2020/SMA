#!/usr/bin/env python
# coding: utf-8

# In[7]:


#setting envoironment 
import numpy as np
import pandas as pd
from pandas_datareader import data
import pandas_datareader as pdr
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[91]:


#Import stock data from yahoo finanace 
CCD = data.DataReader('CCD', 'yahoo',  '1/1/2018')
CCD.head()


# In[92]:


#create a plot
CCD['Close'].plot(grid=True,figsize=(8,5))


# In[93]:


#Rolling method
CCD['42d'] = np.round(CCD['Close'].rolling(window=42).mean(),2)
CCD['252d'] =np.round(CCD['Close'].rolling(window=252).mean(),2)


# In[94]:


CCD.tail


# In[95]:


#closing prices and moving averages
CCD[['Close','42d','252d']].plot(grid=True,figsize=(8,5))


# In[96]:


CCD['42-252'] = CCD['42d'] - CCD['252d']


# In[97]:


X = 50
CCD['Stance'] = np.where(CCD['42-252'] > X, 1, 0)
CCD['Stance'] = np.where(CCD['42-252'] < -X, -1, CCD['Stance'])
CCD['Stance'].value_counts()


# In[98]:


CCD['Stance'].plot(lw=1.5,ylim=[-1.1,1.1])


# In[99]:


CCD['Market Returns'] = np.log(CCD['Close'] / CCD['Close'].shift(1))
CCD['Strategy'] = CCD['Market Returns'] * CCD['Stance'].shift(1)


# In[100]:


CCD[['Market Returns','Strategy']].cumsum().plot(grid=True,figsize=(8,5))


# In[ ]:




