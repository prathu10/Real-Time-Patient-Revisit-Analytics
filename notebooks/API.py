#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import joblib
import pandas as pd


# In[ ]:


import sys
import os
sys.path.append(os.path.dirname('./notebooks'))

from preprocessing import preprocess


# In[3]:


app=Flask(__name__)


# In[ ]:


model = joblib.load("./data/ML Model/readmission_rf_model2.pkl")
model_columns = joblib.load("./data/ML Model/model_columns.pkl")


# In[5]:


THRESHOLD = 0.4 


# In[6]:


@app.route('/')
def home():
    return 'API initialized!'


# In[7]:


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])
        processed_df = preprocess(input_df)
        processed_df = processed_df.reindex(columns=model_columns, fill_value=0)

        probability = model.predict_proba(processed_df)[0][1]
        prediction = 1 if probability > THRESHOLD else 0

        return jsonify({
            "readmitted": "yes" if prediction == 1 else "no",
            "probability": round(probability, 4),
            "threshold_used": THRESHOLD
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:




