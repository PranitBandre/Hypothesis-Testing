#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats as stats
import numpy as np


# In[2]:


df= pd.read_csv('BuyerRatio.csv')
df.head()


# In[3]:


df_table=df.iloc[:,1:6]
df_table


# In[4]:


val=stats.chi2_contingency(df_table)
val


# In[5]:


no_of_rows=len(df_table.iloc[0:2,0])
no_of_columns=len(df_table.iloc[0,0:4])
degree_of_f=(no_of_rows-1)*(no_of_columns-1)
print('Degree of Freedom=',degree_of_f)


# In[6]:


Expected_value=val[3]
Expected_value


# In[7]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2/e for o,e in zip(df_table.values,Expected_value)])
chi_square_statestic=chi_square[0]+chi_square[1]
chi_square_statestic


# In[8]:


critical_value=chi2.ppf(0.95,3)
critical_value


# In[9]:


if chi_square_statestic >= critical_value:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[10]:


pvalue=1-chi2.cdf(chi_square_statestic,3)
pvalue


# In[11]:


if pvalue <= 0.05:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[ ]:




