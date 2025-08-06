# LiveReadmitML-Real-Time-Readmission-Prediction-with-Power-BI

> A real-time hospital readmission prediction system using machine learning, deployed via Flask API, and integrated with Power BI for live analytics and visualization.

---

### 📌 Project Overview

Hospital readmissions are a major indicator of healthcare quality and cost efficiency. This project aims to **predict the likelihood of patient readmission within 30 days** using clinical and demographic data. By combining **scikit-learn**, **Flask**, and **Power BI**, we deliver an end-to-end system for **real-time inference and dashboard monitoring**.

---

### 🧠 Core Objectives

- 🔍 Analyze and preprocess medical data to identify key predictors of readmission.
- 🧪 Train and optimize machine learning models using **scikit-learn v1.7.1**.
- 🚀 Deploy the model through a **Flask API** for real-time prediction requests.
- 📡 Connect the API with **Power BI** for live data visualization and decision-making support.

---

### ⚙️ Features

- ✅ Real-time REST API for prediction (`/predict`)
- ✅ Binary classification: "Readmitted" vs "Not Readmitted"
- ✅ Probability confidence score
- ✅ Power BI dashboard integration
- ✅ Fully compatible with `scikit-learn==1.7.1`

---

### 🧰 Tech Stack

| Category             | Technologies Used                             |
|----------------------|-----------------------------------------------|
| 💻 Machine Learning   | `scikit-learn`, `pandas`, `numpy`             |
| 🧪 Model Algorithms   | Random Forest, Logistic Regression            |
| 🌐 API Deployment     | `Flask`, `joblib`                             |
| 📈 Visualization      | `Power BI` via API integration                |
| 🛠️ Others             | `matplotlib`, `seaborn`, `requests`, `json`  |

---

### 📁 Project Structure


---

### 🧪 Model Training Summary

- **Dataset Used:** [Diabetes Readmission Dataset (UCI/Kaggle)](https://www.kaggle.com/datasets/aaron7sun/diabetes-health-indicators-dataset)
- **Target Variable:** Readmission within 30 days
- **Model:** Random Forest Classifier
- **Accuracy Achieved:** ~82%
- **Metrics Used:** Accuracy, ROC-AUC, Confusion Matrix

---

### 🚀 API Usage

### 🔗 Endpoint

```http
POST /predict
Content-Type: application/json
```
### 📥 Input Payload (Example)
json
```
{
  "age": 45,
  "gender": "Male",
  "admission_type": "Emergency",
  "diagnosis": "Diabetes",
  "num_lab_procedures": 35,
  "num_medications": 12,
  "time_in_hospital": 4,
  "number_outpatient": 0,
  "number_emergency": 1,
  "number_inpatient": 0
}
```
### 📤 API Response
json
```
{
  "readmitted": "yes",
  "probability": 0.8743
}
```

### 📊 Power BI Dashboard
- File: powerbi/powerbi_dashboard.pbix

- Connects live to Flask API

- Dashboards include:

  * Readmission risk by age, diagnosis

  * Risk vs length of stay
  
  * Prediction distribution by type of admission

- To Use:

  * Open the PBIX file in Power BI Desktop.
  
  * Set up the web connection to http://127.0.0.1:5000/predict.
  
  * Input test data via Power BI interface or direct API link.
  
  * View real-time predictions and insights.

### 🛠 Setup Instructions
1. Clone the Repository
bash
```
git clone https://github.com/yourusername/LiveReadmitML-Real-Time-Readmission-Prediction-with-Power-BI.git
cd LiveReadmitML-Real-Time-Readmission-Prediction-with-Power-BI
```

2. Create a Virtual Environment
bash
```
python -m venv env
source env/bin/activate    # For Linux/macOS
env\Scripts\activate       # For Windows
```

3. Install Requirements
bash
```
pip install -r requirements.txt
Ensure scikit-learn==1.7.1 is installed to avoid compatibility issues.
```
4. Start the Flask API Server
bash
```
cd api
python app.py
```

The API will be available at http://localhost:5000/

### 🧪 Power BI Configuration
- Open PowerBI/real-time-dashboard.pbix

- Edit the data source to point to your local Flask API (http://localhost:5000/predict)

- Trigger predictions using sample data and view real-time results

### 🏆 Achievements
📌 Published project titled "LiveReadmitML - Real-Time Readmission Prediction with Power BI" as a real-time hospital analytics solution.

📈 Achieved 82% model accuracy after preprocessing, feature engineering, and hyperparameter tuning.

🌐 Integrated real-time RESTful API with Power BI for predictive healthcare visualization.

### 👨‍💻 Author
Rohitkumar Jha
M.S. in Computer Science – Cybersecurity | The George Washington University
