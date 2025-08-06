#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

print("All libraries loaded successfully!")


# In[ ]:


data = pd.read_csv('./data/hospital_readmissions.csv')
data.info()
data.describe()


# In[4]:


sns.countplot(x='readmitted', data=data)


# In[5]:


data.shape
data.head()


# In[6]:


data.isnull().sum()


# In[7]:


for col in ['time_in_hospital', 'n_lab_procedures', 'n_medications']:
    upper_limit = data[col].quantile(0.99)
    data[col] = data[col].clip(upper=upper_limit)


# In[8]:


data = pd.get_dummies(data, drop_first=True)


# In[9]:


print(data.shape)


# In[10]:


data.head()


# In[11]:


data.isnull().sum()


# In[12]:


for col in ['time_in_hospital', 'n_lab_procedures', 'n_medications']:
    upper_limit = data[col].quantile(0.99)
    data[col] = data[col].clip(upper=upper_limit)


# In[13]:


data = pd.get_dummies(data, drop_first=True)


# In[14]:


data['multiple_visits'] = (
    data['n_inpatient'] + data['n_outpatient'] + data['n_emergency']
) > 1


# In[ ]:


data.to_csv('./data/datacleaned_hospital_readmissions.csv', index=False)
print("Cleaned dataset saved!")


# In[ ]:





# In[ ]:





# In[ ]:




