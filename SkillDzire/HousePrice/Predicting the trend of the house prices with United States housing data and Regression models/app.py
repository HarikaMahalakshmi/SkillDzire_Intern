import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model and training columns
model = joblib.load('house_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')  # list of feature columns used during training

st.title("🏡 House Price Predictor")
st.write("Please fill in the values below to get the house price prediction.")


# Minimal input fields (subset of your training features)
input_data = {
    'MSZoning': st.selectbox('MSZoning', ['RL', 'RM', 'FV', 'RH', 'C (all)']),
    'Street': st.selectbox('Street', ['Pave', 'Grvl']),
    'LotShape': st.selectbox('LotShape', ['Reg', 'IR1', 'IR2', 'IR3']),
    'Neighborhood': st.selectbox('Neighborhood', ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel']),  # Add more as needed
    'LotArea': st.number_input('Lot Area', value=8450),
    'YearBuilt': st.slider('Year Built', 1900, 2025, 2003),
    '1stFlrSF': st.number_input('1st Floor SF', value=856),
    '2ndFlrSF': st.number_input('2nd Floor SF', value=854),
    'GrLivArea': st.number_input('Living Area (sq ft)', value=1710),
    'GarageArea': st.number_input('Garage Area (sq ft)', value=548)
}

# Convert user input to DataFrame
user_df = pd.DataFrame([input_data])

# One-hot encode input (same as training)
user_df_encoded = pd.get_dummies(user_df)

# Add missing columns (that were in training) and ensure correct order
for col in model_columns:
    if col not in user_df_encoded:
        user_df_encoded[col] = 0  # Add missing column with 0

user_df_encoded = user_df_encoded[model_columns]  # reorder to match model

# Predict on aligned input
if st.button("🔮 Predict Price"):
    try:
        prediction = model.predict(user_df_encoded)[0]
        st.success(f"🏷️ Estimated House Price: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
