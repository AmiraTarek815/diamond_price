import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎", layout="centered")

st.markdown(
    "<style>[data-testid='stSidebarNav'] {display: none;}</style>",
    unsafe_allow_html=True
)
 
with st.sidebar:
    st.markdown(
        "<h2 style='color:white; margin-bottom: 20px;'>💎 Diamond Predictor</h2>",
        unsafe_allow_html=True
    )
 
    if st.button("🏠  Home", use_container_width=True):
        st.switch_page("app.py")
 
    if st.button("💰  Predict Price", use_container_width=True):
        st.switch_page("pages/prediction.py")
 
    st.markdown(
        "<a href='/#how-it-works' target='_self' style='"
        "display:block; text-align:center; padding:0.5rem 0; margin-top:0.5rem;"
        "background-color:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.2);"
        "border-radius:8px; color:#EAEAEA; text-decoration:none; font-size:16px; font-weight:500;'>"
        "📘  How it works</a>",
        unsafe_allow_html=True
    )

model = joblib.load('diamond_price.pkl')

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("diamond-13258.png", width=150)

st.markdown(
    "<h2 style='text-align: center;'>Diamond Price Estimator</h2>",
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
    carat = st.number_input("Carat", min_value=0.1, max_value=6.0, value=0.5, step=0.01,
       help="The weight of the diamond. 1 carat = 0.2 grams.")
    cut = st.selectbox("Cut", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'],
      help="How well the diamond is cut, affecting its brilliance and sparkle.")
    color = st.selectbox("Color", ['J', 'I', 'H', 'G', 'F', 'E', 'D'],
        help="Diamond color grade from J (more color) to D (colorless, most valuable).")
    clarity = st.selectbox("Clarity", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'],
        help="Diamond clarity grade from I1 (least clear) to IF (internally flawless).")

with col2:
    st.subheader("Measurements")
    depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=61.5, step=0.1,
       help="Total depth percentage = height of the diamond relative to its width.")
    table = st.number_input("Table", min_value=40.0, max_value=100.0, value=57.0, step=0.1,
       help="Width of the diamond's top flat surface relative to its widest point.")
    volume = st.number_input("Volume (mm³)", min_value=1.0, max_value=1000.0, value=40.0, step=0.1,
        help="Approximate volume of the diamond (length × width × depth).")

st.divider()

if st.button("Price"):
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