import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("employee_retention_model.pkl", "rb"))

# Load encoder
encoder = pickle.load(open("salary_encoder.pkl", "rb"))

st.title("Employee Retention Prediction App")

st.write("Enter employee details below:")

# User Inputs
satisfaction_level = st.slider(
    "Satisfaction Level",
    0.0, 1.0, 0.5
)

average_montly_hours = st.number_input(
    "Average Monthly Hours",
    min_value=50,
    max_value=350,
    value=200
)

promotion_last_5years = st.selectbox(
    "Promotion in Last 5 Years",
    ["Yes", "No"]
)

promotion_last_5years=1 if promotion_last_5years=="Yes" else 0

salary = st.selectbox(
    "Salary Level",
    ["low", "medium", "high"]
)

# Encode salary
salary_encoded = encoder.transform([salary])[0]

# Create dataframe
input_data = pd.DataFrame({
    'satisfaction_level': [satisfaction_level],
    'average_montly_hours': [average_montly_hours],
    'promotion_last_5years': [promotion_last_5years],
    'salary': [salary_encoded]
})

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Employee is likely to leave the company.")
    else:
        st.success("Employee is likely to stay in the company.")