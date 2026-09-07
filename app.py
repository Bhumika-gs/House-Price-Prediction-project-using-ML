import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to estimate its price.")


# Input fields
area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=20000,
    value=5000
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

stories = st.number_input(
    "Number of Stories",
    min_value=1,
    max_value=5,
    value=2
)

parking = st.number_input(
    "Number of Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

mainroad = st.selectbox(
    "Main Road",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)


# Prediction
if st.button("Predict House Price"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    # Convert categorical variables
    input_data = pd.get_dummies(
        input_data,
        columns=[
            "mainroad",
            "guestroom",
            "basement",
            "hotwaterheating",
            "airconditioning",
            "prefarea",
            "furnishingstatus"
        ],
        drop_first=True
    )

    # Match training columns
    input_data = input_data.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated House Price: {prediction:,.2f}"
    )
    