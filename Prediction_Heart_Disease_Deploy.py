# -*- coding: utf-8 -*-
"""
Heart Disease Prediction App
"""

# Importing libraries
import numpy as np
import pickle
import streamlit as st
import time

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the new saved model
loaded_model = pickle.load(open(r"hearttrained_modelfinal.sav", 'rb'))

def heart_disease_prediction(input_data):
    """Predict if a person has heart disease."""
    input_data_array = np.asarray(input_data)
    input_data_array_reshape = input_data_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_array_reshape)
    return "The person does not have heart disease" if prediction[0] == 0 else "The Person has heart disease"

# CSS for styling, animations, and alerts
st.markdown(
    """
    <style>
    body {
        background-image: url('A_futuristic_and_professional_medical-themed_backg.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
        font-family: 'Roboto', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 50px;
        color: #e63946;
        font-weight: bold;
        margin-top: 20px;
        
        animation: fadeIn 2s ease-in-out;
    }
    .title .heart {
        color: #e63946;
        animation: pulse 1.5s infinite;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .alert-disease {
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        background-color: rgba(255, 0, 0, 0.5);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
        animation: alertHeartDisease 2s infinite;
    }
    .alert-no-disease {
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        background-color: rgba(0, 255, 0, 0.5);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
        animation: alertNoHeartDisease 2s infinite;
    }
    .alert-button {
        margin-top: 20px;
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    }
    .alert-button:hover {
        background-color: #2980b9;
        transform: scale(1.1);
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #e63946;
        margin-bottom: 40px;
        animation: fadeIn 2.5s ease-in-out;
    }
    .input-container {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin: 20px auto;
        width: 80%;
        max-width: 800px;
        box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.1);
        animation: fadeIn 3s ease-in-out;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #e63946;
        margin-top: 40px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
    }
    .stButton>button {
        background-color: #f39c12;
        color: #ffffff;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover {
        background-color: black;
        transform: translateY(-2px);
    }
    .divider {
        height: 2px;
        margin: 20px 0;
        background-color: #ffffff;
    }
    .result {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        animation: fadeIn 1.5s ease-in-out;
    }
    .result-disease {
        color: red;
    }
    .result-no-disease {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # App title and header
    st.markdown('<div class="title">Heart Disease Prediction App <span class="heart">❤️</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Provide accurate details below to check for heart disease risk.</div>', unsafe_allow_html=True)

    # Input fields organized using columns for compact layout
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("🧑 Age Value", placeholder="Enter Age in Years")
    with col2:
        sex = st.text_input("⚥ Sex Value", placeholder="1 for Male, 0 for Female")
    with col3:
        cp = st.text_input("❤️ Chest pain type", placeholder="Enter Chest Pain Type")

    col4, col5, col6 = st.columns(3)
    with col4:
        trestbps = st.text_input("🩺 Resting BP", placeholder="Enter Resting BP in mmHg")
    with col5:
        chol = st.text_input("🍔 Cholesterol", placeholder="Enter Cholesterol in mg/dL")
    with col6:
        fbs = st.text_input("🩸 Fasting Sugar", placeholder="1 if > 120 mg/dL, else 0")

    col7, col8, col9 = st.columns(3)
    with col7:
        restecg = st.text_input("📉 Resting ECG", placeholder="Enter ECG Results")
    with col8:
        thalach = st.text_input("💓 Max Heart Rate", placeholder="Enter Maximum Heart Rate")
    with col9:
        exang = st.text_input("🏃 Angina", placeholder="1 if Yes, 0 if No")

    col10, col11, col12 = st.columns(3)
    with col10:
        oldpeak = st.text_input("📊 ST Depression", placeholder="Enter ST Depression")
    with col11:
        slope = st.text_input("🗻 Slope", placeholder="Enter Slope of ST")
    with col12:
        ca = st.text_input("🔬 Major Vessels", placeholder="Enter Number of Major Vessels")

    col13 = st.columns(1)[0]
    with col13:
        thal = st.text_input("🧬 Thalassemia", placeholder="Enter Thalassemia Status")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Prediction Section
    diagnosis = ''
    if st.button("🔍 Heart Disease Test Result"):
        with st.spinner("Analyzing..."):
            try:
                # Convert inputs to float
                input_data = [
                    float(age), float(sex), float(cp), float(trestbps),
                    float(chol), float(fbs), float(restecg), float(thalach),
                    float(exang), float(oldpeak), float(slope), float(ca), float(thal)
                ]

                # Make prediction
                diagnosis = heart_disease_prediction(input_data)

                # Placeholder for the alert
                alert_placeholder = st.empty()

                # Trigger fullscreen alert based on prediction
                if diagnosis == "The Person has heart disease":
                    with alert_placeholder.container():
                        st.markdown(
                            '''
                            <div class="alert-disease">
                                ⚠️ WARNING: Heart Disease Detected! ⚠️
                            </div>
                            ''',
                            unsafe_allow_html=True
                        )
                    time.sleep(3)
                    alert_placeholder.empty()
                else:
                    with alert_placeholder.container():
                        st.markdown(
                            '''
                            <div class="alert-no-disease">
                                ✅ No Heart Disease Detected! ✅
                            </div>
                            ''',
                            unsafe_allow_html=True
                        )
                    time.sleep(3)
                    alert_placeholder.empty()
            except ValueError:
                diagnosis = "Please enter valid numeric values for all fields."

        # Display the diagnosis result in red for heart disease and green for no heart disease
        if diagnosis == "The Person has heart disease":
            st.markdown(f'<div class="result result-disease">{diagnosis}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result result-no-disease">{diagnosis}</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">Heart Disease Prediction App © 2024</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
