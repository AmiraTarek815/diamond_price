import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎", layout="centered")

model = joblib.load('diamond_price.pkl')

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("diamond-13258.png", width=120)

st.markdown(
    "<h2 style='text-align: center;'>Diamond Price Predictor</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Enter the diamond's specifications to predict its price.</p>",
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Diamond details")
    carat = st.number_input("Carat", min_value=0.1, max_value=6.0, value=0.5, step=0.01)
    cut = st.selectbox("Cut", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox("Color", ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox("Clarity", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

with col2:
    st.subheader("Measurements")
    depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=61.5, step=0.1)
    table = st.number_input("Table", min_value=40.0, max_value=100.0, value=57.0, step=0.1)
    volume = st.number_input("Volume (mm³)", min_value=1.0, max_value=1000.0, value=40.0, step=0.1)

st.divider()

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'volume': [volume]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Diamond Price: **${prediction:,.2f}**")