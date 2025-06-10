# codebasics ML course: codebasics.io, all rights reserved

import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

# Page title
st.title("💰 Health Insurance Cost Predictor")

# Description
st.markdown("""
This tool estimates your **annual health insurance premium** based on personal, lifestyle, and medical factors.
Fill in your details below and click **Predict** to get an estimate.
""")

# Begin form
with st.form("input_form"):

    st.header("👤 Personal & Financial Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
    with col2:
        number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20, step=1)
    with col3:
        income_lakhs = st.number_input("Income (in Lakhs)", min_value=0, max_value=200, step=1)

    st.header("🧬 Medical & Lifestyle Information")
    col4, col5, col6 = st.columns(3)
    with col4:
        genetical_risk = st.number_input("Genetical Risk Score (0–5)", min_value=0, max_value=5, step=1)
    with col5:
        bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
    with col6:
        smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])

    col7, col8, col9 = st.columns(3)
    with col7:
        gender = st.selectbox("Gender", ['Male', 'Female'])
    with col8:
        marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
    with col9:
        region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

    col10, col11, col12 = st.columns(3)
    with col10:
        medical_history = st.selectbox("Medical History", [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ])
    with col11:
        employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer', ''])
    with col12:
        insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

    # Prepare input
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    # Submit button inside form
    submitted = st.form_submit_button("🎯 Predict")

# Prediction result
if submitted:
    prediction = predict(input_dict)
    st.success(f"💡 Estimated Annual Health Insurance Cost: ₹ {prediction:,}")
