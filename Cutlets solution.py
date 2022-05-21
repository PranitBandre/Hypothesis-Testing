#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[7]:


data=pd.read_csv('Cutlets.csv')
data.head()


# In[8]:


unitA=pd.Series(data.iloc[:,0])
unitB=pd.Series(data.iloc[:,1])


# In[9]:


p_value=stats.ttest_ind(unitA,unitB)
p_value


# In[12]:


p_value[1]


# In[ ]:


##Note

#  Varify p_value with α = 0.05 (At 5% significance level)
#  Assume Null hyposthesis as Ho: μ1 = μ2 (There is no difference in diameters of cutlets between two units).

#  Thus Alternate hypothesis as Ha: μ1 ≠ μ2 (There is significant difference in diameters of cutlets between two units) 2 Sample 2 Tail test applicable

