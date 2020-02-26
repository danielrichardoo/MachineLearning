#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

listingData = pd.read_csv("listings.csv")


# In[20]:


print(listingData)


# In[15]:


maxValue = listingData.max()
print(maxValue)


# In[16]:


minValue = listingData.min()
print(minValue)


# In[18]:


newListingDataDrop = listingData.dropna()
print(newListingDataDrop)


# In[19]:


newListingDataFill = listingData.fillna('thisIsNULL')
print(newListingDataFill)


# In[ ]:




