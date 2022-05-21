#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2


# In[2]:


customer= pd.read_csv('Costomer+OrderForm.csv')
customer.head()


# In[3]:


print(customer['Phillippines'].value_counts(),customer['Indonesia'].value_counts(),customer['Malta'].value_counts(),customer['India'].value_counts())


# In[4]:


observed=([[271,267,269,280],[29,33,31,20]])
observed


# In[5]:


stat, p, dof, expected = chi2_contingency([[271,267,269,280],[29,33,31,20]])
stat


# In[6]:


p


# In[7]:


print('dof=%d' % dof)
print(expected)


# In[8]:


alpha = 0.05
prob=1-alpha
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0),variables are related')
else:
	print('Independent (fail to reject H0), variables are not related')


# In[9]:


print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[ ]:




