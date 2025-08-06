#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

print("All libraries loaded successfully!")


# In[5]:


import sklearn
print("scikit-learn version:", sklearn.__version__)


# In[ ]:


data = pd.read_csv('./data/datacleaned_hospital_readmissions.csv')
data.head()


# In[7]:


x= data.drop('readmitted_yes', axis=1)
y= data['readmitted_yes']


# In[8]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42, stratify=y)


# In[9]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score


# In[10]:


logreg = LogisticRegression(max_iter=1000)
logreg.fit(x_train, y_train)

y_predict_lr=logreg.predict(x_test)
y_probability_lr=logreg.predict_proba(x_test)[:,1]

print("Logistic Regression Performance Summary:")
print(classification_report(y_test, y_predict_lr))
print("ROC-AUC Score:", roc_auc_score(y_test, y_probability_lr))


# In[11]:


from sklearn.ensemble import RandomForestClassifier


# In[12]:


rf = RandomForestClassifier(random_state=42)
rf.fit(x_train, y_train)

y_predict_rf=rf.predict(x_test)
y_probability_rf=rf.predict_proba(x_test)[:,1]

print("Logistic Regression Performance Summary:")
print(classification_report(y_test, y_predict_rf))
print("ROC-AUC Score:", roc_auc_score(y_test, y_probability_rf))


# In[13]:


rf = RandomForestClassifier(random_state=42, class_weight='balanced')


# In[14]:


from sklearn.model_selection import GridSearchCV


# In[15]:


para_grid={'n_estimators': [100,200,300], 'max_depth': [None,10,20], 'min_samples_split': [2,5]}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42, class_weight='balanced'), para_grid, cv=3, scoring='roc_auc')
grid_search.fit(x_train, y_train)
best_rf=grid_search.best_estimator_


# In[16]:


print("Best Parameters Found:", grid_search.best_params_)
print("Best ROC-AUC Score:", grid_search.best_score_)


# In[17]:


results_df = pd.DataFrame(grid_search.cv_results_)
results_df = results_df[['params', 'mean_test_score', 'std_test_score', 'rank_test_score']]
results_df = results_df.sort_values(by='mean_test_score', ascending=False)
results_df.head()


# In[18]:


results_df['n_estimators'] = results_df['params'].apply(lambda x: x['n_estimators'])
results_df['max_depth'] = results_df['params'].apply(lambda x: x['max_depth'])
pivot_table = results_df.pivot_table( values='mean_test_score', index='max_depth', columns='n_estimators')
plt.figure(figsize=(8, 6))
sns.heatmap( pivot_table, annot=True, fmt=".4f", cmap="YlGnBu")
plt.title('Grid Search ROC-AUC Heatmap\n(max_depth vs n_estimators)')
plt.xlabel('n_estimators')
plt.ylabel('max_depth')
plt.show()


# In[19]:


best_params = grid_search.best_params_
best_auc = grid_search.best_score_
print("Best Params:", best_params, "| Best ROC-AUC:", best_auc)


# In[ ]:


import joblib
joblib.dump(best_rf, './data/ML Model/readmission_rf_model2.pkl')
joblib.dump(x_train.columns.tolist(), './data/ML Model/model_columns.pkl')


# In[ ]:





# In[ ]:




