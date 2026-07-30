import streamlit as st
import base64
from nav import render_sidebar

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎", layout="wide")

# ---------- Custom background image ----------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("background (2).jpg")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(5,5,10,0.55), rgba(5,5,10,0.7)), url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar navigation ----------
render_sidebar()

# ---------- Hero section ----------
st.markdown(
    "<h1 style='text-align: center; color: white; margin-top: 40px;'>Diamond Price Predictor</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #C9C9D1; font-size: 18px;'>"
    "Get an instant, data-driven price estimate for any diamond in seconds."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; color: #D5D5DE; font-size: 16px; max-width: 700px; margin: 0 auto;'>"
    "Diamonds are valued based on four key factors known as the 4Cs: carat (weight), cut (how well it's "
    "shaped and faceted), color (how colorless it is), and clarity (how free it is of internal flaws). "
    "Together with a few physical measurements, these factors determine how much a diamond is worth."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- Feature highlights ----------
st.markdown(
    "<h3 style='text-align: center; color: white;'>Why use this app?</h3>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)
card_style = "background-color:rgba(255,255,255,0.08); padding:24px; border-radius:16px; text-align:center; border:1px solid rgba(255,255,255,0.15);"

with c1:
    st.markdown(
        f"<div style='{card_style}'>"
        "<b style='color:white; font-size:17px;'>98% accurate</b><br>"
        "<span style='color:#D5D5DE;'>Trained on 50,000+ real diamonds</span>"
        "</div>", unsafe_allow_html=True
    )
with c2:
    st.markdown(
        f"<div style='{card_style}'>"
        "<b style='color:white; font-size:17px;'>Instant results</b><br>"
        "<span style='color:#D5D5DE;'>Get a price estimate in one click</span>"
        "</div>", unsafe_allow_html=True
    )
with c3:
    st.markdown(
        f"<div style='{card_style}'>"
        "<b style='color:white; font-size:17px;'>Machine learning powered</b><br>"
        "<span style='color:#D5D5DE;'>Built with a Gradient Boosting model</span>"
        "</div>", unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- How it works section ----------
st.markdown(
    "<h3 id='how-it-works' style='text-align: center; color: white;'>How it works</h3>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

h1, h2, h3 = st.columns(3)
step_style = "background-color:rgba(255,255,255,0.08); padding:24px; border-radius:16px; text-align:center; border:1px solid rgba(255,255,255,0.15);"

with h1:
    st.markdown(
        f"<div style='{step_style}'>"
        "<b style='color:white; font-size:17px;'>1. Enter details</b><br>"
        "<span style='color:#D5D5DE;'>Input the diamond's carat, cut, color, clarity and measurements</span>"
        "</div>", unsafe_allow_html=True
    )
with h2:
    st.markdown(
        f"<div style='{step_style}'>"
        "<b style='color:white; font-size:17px;'>2. Model predicts</b><br>"
        "<span style='color:#D5D5DE;'>A Gradient Boosting model trained on 50,000+ diamonds estimates the price</span>"
        "</div>", unsafe_allow_html=True
    )
with h3:
    st.markdown(
        f"<div style='{step_style}'>"
        "<b style='color:white; font-size:17px;'>3. Get instant result</b><br>"
        "<span style='color:#D5D5DE;'>See the predicted price immediately, no waiting</span>"
        "</div>", unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Diamond's Price", use_container_width=True):
        st.switch_page("pages/prediction.py")