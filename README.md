# Social Media Safety & Harassment Prediction 🛡️📊

An end-to-end Data Science and Machine Learning project designed to analyze user behavior on social media and predict the likelihood of online harassment. This project combines comprehensive exploratory data analysis via Power BI dashboards with a predictive machine learning application deployed using Streamlit.

### 🌐 Live Demo
**Check out the live web application here:** [Social Media Harassment Prediction App](https://social-media-harassment-prediction-website.streamlit.app/)

---

## 🎯 Project Overview

With the rapid increase in digital interactions, online safety is a critical concern. This project serves a dual purpose:
1. **Descriptive Analytics:** Utilizing Power BI to uncover patterns regarding demographics, usage behavior, and exposure to inappropriate content.
2. **Predictive Analytics:** An interactive web application that evaluates user inputs (such as privacy settings, platform usage, and demographic data) to classify their risk of experiencing online harassment.

---

## ✨ Key Features

### 1. Power BI Dashboards (Descriptive BI)
The project includes a robust suite of dashboards analyzing:
* **Demographics and Usage Behavior:** Screen time, platform distribution (Facebook, Instagram, Twitter, etc.), and user demographics.
* **Interactions with Unknown Users:** Frequencies of accepting stranger requests and sharing personal information.
* **Exposure to Inappropriate Content:** Tracking encounters with offensive media and derogatory remarks.

### 2. Machine Learning Application (Predictive ML)
An interactive frontend built with Streamlit (`app.py`) that acts as a risk assessment tool. 
* **Target Variable Classification:** 
    * 🟢 Not Harassed
    * 🟡 Moderately Harassed
    * 🔴 Highly Harassed
* **Model Selection:** Evaluated multiple algorithms including Logistic Regression, Naive Bayes, and Support Vector Machines (SVM). **Random Forest** was selected as the final production model due to its superior accuracy and ability to handle non-linear behavioral data.

---

## 🧠 Methodology & Pipeline

1.  **Data Cleaning & Preprocessing:** Handled missing values, encoded categorical variables, and standardized numerical inputs.
2.  **Exploratory Data Analysis (EDA):** Conducted in `eda.ipynb` to find correlations between screen time, age, and harassment frequency.
3.  **Feature Engineering:** Selected the most impactful features contributing to online vulnerability.
4.  **Model Training & Tuning:** Trained various classification models, optimizing hyperparameters for the Random Forest classifier.
5.  **Serialization:** Exported the trained model (`final_model.pkl`) and data scaler (`scaler.pkl`) for deployment.
6.  **Deployment:** Built a user-friendly form interface using Streamlit to accept real-time input and output instant risk predictions.

---

## 📂 Repository Structure

```text
├── app.py                 # Streamlit frontend application for ML predictions
├── eda.ipynb              # Jupyter Notebook containing Data Cleaning and EDA
├── final_model.pkl        # Serialized Random Forest classification model
├── scaler.pkl             # Serialized scaler for feature normalization
├── requirements.txt       # Python dependencies required to run the project
└── README.md              # Project documentation
