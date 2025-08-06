#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[ ]:


def preprocess(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the same preprocessing steps as used during training:
    - fill missing
    - get_dummies
    """
    df = df_raw.copy()
    df.fillna("None", inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    return df


# In[ ]:





# In[ ]:





# In[ ]:




