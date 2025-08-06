#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

patient = {
    "race": "Caucasian",
    "gender": "Female",
    "age": "[70-80]",
    "time_in_hospital": 5,
    "num_lab_procedures": 41,
    "num_procedures": 0,
    "num_medications": 8,
    "number_outpatient": 0,
    "number_emergency": 0,
    "number_inpatient": 0,
    "diag_1": "250.83",
    "diag_2": "401.9",
    "diag_3": "276",
    "number_diagnoses": 9,
    "max_glu_serum": "None",
    "A1Cresult": ">8",
    "metformin": "No",
    "insulin": "No",
    "change": "Ch",
    "diabetesMed": "Yes"
}

response = requests.post("http://127.0.0.1:5000/predict", json=patient)

print("Status Code:", response.status_code)
try:
    print("Prediction:", response.json())
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Response:", response.text)

