# Real-Time-Patient-Revisit-Analytics

> An end-to-end machine learning system for predicting hospital readmissions in real time, deployed using Flask API and connected to Power BI for live reporting and visualization.
---

### 📌 Project Overview

Hospital readmissions are a critical measure of healthcare efficiency and cost. This project focuses on forecasting whether a patient will be readmitted within 30 days based on demographic and clinical information. Leveraging scikit-learn, Flask, and Power BI, the solution provides real-time predictions alongside interactive dashboards for monitoring outcomes.

---

### 🧠 Key Goals

- 🔎 Clean, transform, and analyze patient data to identify major risk factors.
- 🧪 Train and fine-tune ML models using **scikit-learn v1.7.1**.
- 🚀 Expose the model through a Flask-based REST API for instant inference.
- 📡 Integrate with Power BI to deliver real-time decision support via dashboards.
---

### ⚙️ Main Features

- ✅ Real-time API endpoint for predictions (`/predict`)
- ✅ Binary output: "Readmitted" or "Not Readmitted"
- ✅ Seamless Power BI integration for live analytics
- ✅ Probability score for prediction confidence
- ✅ Built with `scikit-learn==1.7.1` for compatibility

---

### 🧰 Tech Stack

| Category             | Technologies Used                             |
|----------------------|-----------------------------------------------|
| 💻 Machine Learning   | `scikit-learn`, `numpy`, `pandas`,              |
| 🧪 Model Algorithms   | Random Forest, Logistic Regression            |
| 🌐 API Deployment     | `Flask`, `joblib`                             |
| 📈 Visualization      | `Power BI` through API integration                |
| 🛠️ Others             | `matplotlib`, `seaborn`, `requests`, `json`  |

---

### 📁 Project Structure


---

### 🧪 Model Development

- **Dataset Used:** [Diabetes Readmission Dataset (UCI/Kaggle)](https://www.kaggle.com/datasets/aaron7sun/diabetes-health-indicators-dataset)
- **Target Variable:** Readmission within 30 days
- **Primary Model:** Random Forest Classifier
- **Accuracy:** ~82%
- **Evaluation Metrics:** Accuracy, ROC-AUC, Confusion Matrix

---

### 🚀 API Usage

### 🔗 Endpoint

```http
POST /predict
Content-Type: application/json
```
### 📥 Example Input:
json
```
{
  "age": 72,
  "gender": "Female",
  "admission_type": "Elective",
  "diagnosis": "Hypertension",
  "num_lab_procedures": 20,
  "num_medications": 8,
  "time_in_hospital": 3,
  "number_outpatient": 1,
  "number_emergency": 0,
  "number_inpatient": 1
}

```
### 📤 API Response
json
```
{
  "readmitted": "no",
  "probability": 0.2317
}
```

### 📊 Power BI Dashboard
- File: data/livepredictions_visualization.pbix

- Connects live to Flask API

- Dashboards include:

  * Risk distribution by age and diagnosis

  * Risk vs length of stay
  
  * Prediction distribution by type of admission

- To Use:

  *Open .pbix file in Power BI Desktop

  *Point the data source to http://127.0.0.1:5000/predict

  *Provide test inputs via Power BI or API request

  *View live predictions and insights

### 🛠 Setup Instructions
1. Clone the Repository
bash
```
git clone https://github.com/prathu10/Real-Time-Patient-Revisit-Analytics.git
cd Real-Time-Patient-Revisit-Analytics
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

### 🧪 Configure Power BI
- Open PowerBI/real-time-dashboard.pbix

- Edit the data source to point to your local Flask API (http://localhost:5000/predict)

- Trigger predictions using sample data and view real-time results

### 🏆 Highlights
📌 Built as a real-time healthcare analytics solution for hospital readmission prediction.

📈 Achieved 82% prediction accuracy with thorough preprocessing and hyperparameter tuning.

🌐 Fully integrated REST API + Power BI dashboards for interactive healthcare insights.

## 🙌 Connect with me on [LinkedIn] — feel free to reach out with any questions, suggestions, or if you'd like to collaborate on adding new features!
## Author: Prathamesh Sonawane
Contact: [LinkedIn](https://www.linkedin.com/in/prathsonawane/) | prathamesh4402@gmail.com


