import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load('calories_model.pkl')

st.title("🔥 Calories Burnt Predictor")

# User inputs
gender = st.selectbox("Gender", ["male", "female"])
age = st.number_input("Age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=30.0)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40)
duration = st.number_input("Workout Duration (minutes)", min_value=0.0)

# Convert gender to number if your model expects numeric
gender_num = 0 if gender == "male" else 1

if st.button("Predict Calories"):
    input_data = np.array([[gender_num, age, weight, height, heart_rate, duration]])
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burnt: {prediction[0]:.2f}")
