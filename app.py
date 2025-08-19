import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('fraud_detection_model.pkl')

# Page config
st.set_page_config(page_title="Fraud Detection Prediction App", page_icon="💳", layout="centered")

# App Title
st.title("💳 Fraud Detection Prediction App")
st.markdown("Enter the transaction details below and click **Predict** to check if the transaction is fraudulent.")






transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Prediction button
if st.button("🔍 Predict", use_container_width=True):
    # Prepare input data
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.subheader("🔎 Prediction Result")
    if prediction == 1:
        st.error("⚠️ This transaction is **likely fraudulent**.")
    else:
        st.success("✅ This transaction is **likely legitimate**.")
