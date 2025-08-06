#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import time
import json


# In[ ]:


data = pd.read_csv('./data/datacleaned_hospital_readmissions.csv')
data.head()


# In[3]:


features = data.drop('readmitted_yes', axis=1)
print(f"Simulating {len(features)} patient records...\n")


# In[4]:


for index,row in features.iterrows():
    patient_data=row.to_dict()
    json_data=json.dumps(patient_data)

    print(f"Send patient record{index+1}:")
    print(json_data)

    time.sleep(5)


# In[ ]:


while True:
    for index, row in features.iterrows():
        patient_data = row.to_dict()
        json_data = json.dumps(patient_data)
        print(json_data)
        time.sleep(2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




