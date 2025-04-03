import streamlit as st
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Linear Regression Prediction App")
st.write("Enter the values to predict the output:")
feature_value = st.number_input("Enter the feature value:", value=0.0, step=0.1)
if st.button("Predict"):
    prediction = model.predict([[feature_value]])[0][0]
    st.write(f"The predicted output is: {prediction[0]:.2f}") 



