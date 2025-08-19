import streamlit as st
import pandas as pd
import joblib
import os
import sys

# 🔹 If your model was trained with custom transformers/classes, import them here
# from my_module import MyCustomTransformer, MyCustomEncoder

# Optional: print environment info for debugging (remove in production)
print("Python:", sys.version)
print("Working dir:", os.getcwd())

# 🔹 Use absolute path to avoid relative path issues
MODEL_PATH = os.path.join(os.path.dirname(__file__), "fraud_detection_model.pkl")

# Load the trained model safely
try:
    model = joblib.load(MODEL_PATH)
except AttributeError as e:
    st.error(f"Model loading failed: {e}")
    st.stop()
except FileNotFoundError:
    st.error("Model file not found. Please check the path.")
    st.stop()

# Page config
st.set_page_config(
    page_title="Fraud Detection Prediction App",
    page_icon="💳",
    layout="centered"
)

# App Title
st.title("💳 Fraud Detection Prediction App")
st.markdown(
    "Enter the transaction details below and click **Predict** "
    "to check if the transaction is fraudulent."
)

# Input fields
transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)
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

    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    st.subheader("🔎 Prediction Result")
    if prediction == 1:
        st.error("⚠️ This transaction is **likely fraudulent**.")
    else:
        st.success("✅ This transaction is **likely legitimate**.")
