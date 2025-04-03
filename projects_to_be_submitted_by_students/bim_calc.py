import streamlit as st
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        div.stSlider { 
            background: #ffffff; 
            padding: 10px; 
            border-radius: 10px; 
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        .stMetric {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: #ff3fff;'>BMI Calculator 🏋️‍♂️</h1>", unsafe_allow_html=True)

# Input Section
st.sidebar.header("Enter Your Details:")
height = st.sidebar.slider("Height (cm)", 100, 250, 170)
weight = st.sidebar.slider("Weight (kg)", 30, 200, 70)

# BMI Calculation
bmi = weight / (height / 100) ** 2

# Display BMI
st.subheader("Your BMI Result:")
st.metric(label="Body Mass Index (BMI)", value=f"{bmi:.2f}")

# Determine BMI Category
if bmi < 18.5:
    category = "Underweight 😔"
    st.warning("You are underweight. Consider a balanced diet! 🍎")
elif 18.5 <= bmi < 25:
    category = "Normal weight ✅"
    st.success("Great! You have a healthy BMI! 🥦")
elif 25 <= bmi < 30:
    category = "Overweight ⚠️"
    st.warning("You are overweight. Consider regular exercise! 🏃‍♂️")
else:
    category = "Obesity ❌"
    st.error("Obesity detected! Prioritize a healthier lifestyle. 🏥")

# Show BMI Category
st.subheader(f"Category: {category}")

# BMI Categories Table
st.markdown("""
### BMI Categories 📊
| Category       | BMI Range |
|---------------|------------|
| Underweight   | BMI < 18.5 |
| Normal weight | 18.5 - 24.9 |
| Overweight    | 25 - 29.9 |
| Obesity       | BMI ≥ 30 |
""", unsafe_allow_html=True)
