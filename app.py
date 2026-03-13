import streamlit as st
import pickle
import pandas as pd

st.title("Employment Prediction App")

# Load model
model = pickle.load(open("model.pkl","rb"))

# User inputs
age = st.number_input("Enter Age")
experience = st.number_input("Enter Experience")

# Prediction button
if st.button("Predict"):

    data = pd.DataFrame({
        "age":[age],
        "experience":[experience]
    })

    prediction = model.predict(data)

    st.success(f"Prediction: {prediction[0]}")
