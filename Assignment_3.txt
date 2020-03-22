#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


airbnb = pd.read_csv("listings.csv")
print(airbnb.dtypes)
print(airbnb.isna().values.any())


# In[3]:


newAirbnbDiscrete = airbnb[["minimum_nights"]]
newAirbnbContinue = airbnb[["latitude", "longitude", "price", "number_of_reviews", "reviews_per_month", "calculated_host_listings_count", "availability_365"]]

print("Discrete : \n{}\n\n\n".format(newAirbnbDiscrete.head()))
print("Continue : \n{}\n\n\n".format(newAirbnbContinue.head()))


# In[4]:


# Discrete
print("Discrete : ")
print("mean = {}\n".format(newAirbnbDiscrete.mean()))
print("variance = {}\n".format(np.var(newAirbnbDiscrete)))
#Continue
print("Continue : ")
print("mean = {}\n".format(newAirbnbContinue.mean()))
print("variance = {}\n".format(np.var(newAirbnbContinue)))


# In[ ]:




