#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[5]:


data=pd.read_csv('LabTAT.csv')
data.head()


# In[6]:


# Anova ftest statistics
p_value=stats.f_oneway(data.iloc[:,0],data.iloc[:,1],data.iloc[:,2],data.iloc[:,3])
p_value


# In[7]:


p_value[1]


# In[ ]:


#compare it with α = 0.05

#Anova ftest statistics: Analysis of varaince between more than 2 samples or columns Assume Null Hypothesis Ho as No Varaince: All samples TAT population means are same

#Thus Alternate Hypothesis Ha as It has Variance: Atleast one sample TAT population mean is different

