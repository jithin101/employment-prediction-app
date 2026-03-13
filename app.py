import streamlit as st
import joblib
import pandas as pd

st.title("Employment Prediction App")

model = joblib.load("model.pkl")

age = st.number_input("Age")
experience = st.number_input("Experience")

if st.button("Predict"):
    
    data = pd.DataFrame({
        "age":[age],
        "experience":[experience]
    })
    
    prediction = model.predict(data)
    
    st.success(prediction)
