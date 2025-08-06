#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import random
import time
import json
import os
import csv

os.makedirs("notebooks", exist_ok=True)
url = "https://api.fda.gov/drug/event.json?search=seriousnesshospitalization:1&limit=1"
csv_path = "./data/livepredictions.csv"

age_groups = [
    "[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
    "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"
]
age_index = 0

def generate_high_risk_patient(age_label):
    gender = random.choice(["Male", "Female"])

    return {
        "race": "Caucasian",
        "gender": gender,
        "age": age_label,
        "time_in_hospital": random.randint(10, 14),           
        "num_lab_procedures": random.randint(70, 100),        
        "num_procedures": random.randint(3, 6),               
        "num_medications": random.randint(40, 50),            
        "number_outpatient": random.randint(5, 10),           
        "number_emergency": random.randint(2, 5),             
        "number_inpatient": random.randint(5, 10),            
        "diag_1": "250.83",
        "diag_2": "428.0",
        "diag_3": "518.81",
        "number_diagnoses": random.randint(8, 10),            
        "max_glu_serum": "None",
        "A1Cresult": ">8",                                  
        "metformin": "Yes",
        "insulin": "Up",
        "change": "Ch",
        "diabetesMed": "Yes"
    }

while True:
    try:
        use_risky = random.random() < 0.4
        current_age = age_groups[age_index]
        age_index = (age_index + 1) % len(age_groups)

        if use_risky:
            model_input = generate_high_risk_patient(current_age)
        else:
            res = requests.get(url)
            record = res.json()["results"][0]
            patient_data = record.get("patient", {})
            age = patient_data.get("patientonsetage", random.randint(30, 80))
            gender_code = patient_data.get("patientsex", "0")
            gender = "Male" if gender_code == "1" else "Female" if gender_code == "2" else "Unknown"
            model_input = {
                "race": "Caucasian",
                "gender": gender,
                "age": current_age,
                "time_in_hospital": random.randint(1, 14),
                "num_lab_procedures": random.randint(1, 100),
                "num_procedures": random.randint(0, 6),
                "num_medications": random.randint(1, 50),
                "number_outpatient": random.randint(0, 10),
                "number_emergency": random.randint(0, 5),
                "number_inpatient": random.randint(0, 10),
                "diag_1": random.choice(["250.83", "401.9", "276"]),
                "diag_2": random.choice(["428.0", "414.01", "250.01"]),
                "diag_3": random.choice(["518.81", "584.9", "530.81"]),
                "number_diagnoses": random.randint(1, 10),
                "max_glu_serum": "None",
                "A1Cresult": random.choice([">8", "None", ">7"]),
                "metformin": random.choice(["Yes", "No"]),
                "insulin": random.choice(["No", "Steady", "Up", "Down"]),
                "change": random.choice(["Ch", "No"]),
                "diabetesMed": random.choice(["Yes", "No"])
            }

        prediction = requests.post("http://127.0.0.1:5000/predict", json=model_input).json()
        print(f"Age: {model_input['age']} → Prediction:", prediction)

        file_exists = os.path.isfile(csv_path)
        with open(csv_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    "gender", "age", "time_in_hospital", "num_medications",
                    "probability", "readmitted"
                ])
            writer.writerow([
                model_input["gender"],
                model_input["age"],
                model_input["time_in_hospital"],
                model_input["num_medications"],
                prediction.get("probability", None),
                prediction.get("readmitted", None),
                "Yes" if use_risky else "No"
            ])

    except Exception as e:
        print("Error:", e)

    time.sleep(5)

