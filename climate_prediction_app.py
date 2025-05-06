import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load the saved Linear Regression model

model_path = '/content/linear_regression_model.pkl'  
linear_model = joblib.load(model_path)
linear_model = joblib.load(model_path)

# Set Streamlit page configuration
st.set_page_config(page_title="Climate Predictions in Tanzania", layout="wide")

# Sidebar for navigation
st.sidebar.title("Climate Prediction App")
app_mode = st.sidebar.radio("Navigate", ["Home", "EDA", "Predict"])

# Home Section
if app_mode == "Home":
    st.title("Climate Prediction in Tanzania")
    st.write("""
    This app uses historical climate data to predict future climate conditions in Tanzania.
    Explore the interactive visualizations and make real-time predictions using the machine learning model.
    """)

    # Add an image or banner
    st.image("https://images.unsplash.com/photo-1571558826400-ecfcb51a3b94", caption="Climate and Weather Trends", use_column_width=True)

# EDA Section
elif app_mode == "EDA":
    st.title("Exploratory Data Analysis (EDA)")
    st.write("Visualizations of historical climate trends in Tanzania.")

    # Load example plots (replace with actual plots)
    st.image("/content/predicted_temperatures_plot.png", caption="Predicted Temperatures")
    st.image("/content/feature_importance_rf.png", caption="Feature Importance")

# Predict Section
elif app_mode == "Predict":
    st.title("Predict Future Climate Conditions")
    st.write("Enter the climate parameters to predict the average temperature.")

    # Input sliders for user parameters
    Total_Rainfall_mm = st.slider("Total Rainfall (mm)", 0, 500, 100)
    Max_Temperature_C = st.slider("Max Temperature (°C)", 20, 50, 30)
    Min_Temperature_C = st.slider("Min Temperature (°C)", 10, 30, 20)
    Temp_Range_C = Max_Temperature_C - Min_Temperature_C
    Rainfall_3M = st.slider("Rainfall (3-Month Rolling Average, mm)", 0, 1000, 300)

    # Seasonal dropdowns
    season = st.selectbox("Season", ["Spring", "Summer", "Winter"])
    Season_Spring = 1 if season == "Spring" else 0
    Season_Summer = 1 if season == "Summer" else 0
    Season_Winter = 1 if season == "Winter" else 0

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'Total_Rainfall_mm': [Total_Rainfall_mm],
        'Max_Temperature_C': [Max_Temperature_C],
        'Min_Temperature_C': [Min_Temperature_C],
        'Temp_Range_C': [Temp_Range_C],
        'Rainfall_3M': [Rainfall_3M],
        'Season_Spring': [Season_Spring],
        'Season_Summer': [Season_Summer],
        'Season_Winter': [Season_Winter]
    })

    # Predict button
    if st.button("Predict"):
        prediction = linear_model.predict(input_data)[0]
        st.success(f"Predicted Average Temperature: {prediction:.2f}°C")
