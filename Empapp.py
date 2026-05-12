import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open('employee_model.pkl', 'rb'))

# Page Config
st.set_page_config(
    page_title="Employee Retention Prediction",
    layout="centered"
)

# Title
st.title("Employee Retention Prediction")
st.write("Predict whether an employee will stay or leave the company.")

st.divider()

# Satisfaction Level
satisfaction_level = st.number_input(
    "Satisfaction Level (0 to 1)",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

# Average Monthly Hours
average_montly_hours = st.number_input(
    "Average Monthly Hours",
    min_value=50,
    max_value=350,
    value=150,
    step=1
)

# Promotion
promotion_last_5years = st.selectbox(
    "Promotion in Last 5 Years",
    ["No", "Yes"]
)

promotion_last_5years = 1 if promotion_last_5years == "Yes" else 0

# Salary
salary = st.selectbox(
    "Salary Level",
    ["low", "medium", "high"]
)
# Salary Encoding
salary_low = 0
salary_medium = 0
salary_high = 0

if salary == "low":
    salary_low = 1

elif salary == "medium":
    salary_medium = 1

elif salary == "high":
    salary_high = 1

# Create DataFrame
input_data = pd.DataFrame({
    'satisfaction_level': [satisfaction_level],
    'average_montly_hours': [average_montly_hours],
    'promotion_last_5years': [promotion_last_5years],
    'salary_low': [salary_low],
    'salary_medium': [salary_medium]
})

st.divider()

# Prediction Button
if st.button("Predict Employee Retention"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Employee may leave the company")

    else:
        st.success("Employee is likely to stay")