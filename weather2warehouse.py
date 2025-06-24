'''
import streamlit as st
import base64

def set_local_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_local_background("image.jpeg") 

st.title("Weather2Warehouse 🌦️")
st.subheader("Smart product stocking based on weather forecasts")

weather_products = {
    "Rain": ["Umbrellas", "Raincoats", "Waterproof shoes"],
    "Sunny": ["Sunglasses", "Sunscreen", "Cold drinks"],
    "Cold": ["Heaters", "Woollen clothes", "Hot beverages"],
    "Hot": ["Cold drinks", "ACs/Fans", "Cotton clothes"],
    "Storm": ["Emergency lights", "Dry foods", "Power banks"]
}

weather = st.selectbox("Select upcoming weather condition:", list(weather_products.keys()))

if st.button("Suggest Products"):
    st.success("Based on the forecast, you should stock:")
    for item in weather_products[weather]:
        st.markdown(f"- {item}")
'''

import streamlit as st
import base64

def set_local_background(image_file, fade=0.5):
    """
    image_file : str  → local file name (png / jpg / jpeg)
    fade       : float→ 0 = fully transparent overlay, 1 = solid color;
                           0.5 ≈ 50 % image opacity
    """
    mime = "png" if image_file.lower().endswith("png") else "jpeg"
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    # RGBA overlay color (white here). 0.5 = 50 % opacity
    overlay_rgba = f"rgba(255,255,255,{fade})"

    st.markdown(
        f"""
        <style>
        .stApp {{
            /* first layer = translucent overlay,
               second layer = your image              */
            background-image:
               linear-gradient({overlay_rgba}, {overlay_rgba}),
               url("data:image/{mime};base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────
set_local_background("image.jpeg", fade=0.4)   # 40 % white overlay
# ─────────────────────────────────────────────────────────

st.title("Weather2Warehouse 🌦️")
st.subheader("Smart product stocking based on weather forecasts")

weather_products = {
    "Rain":  ["Umbrellas", "Raincoats", "Waterproof shoes"],
    "Sunny": ["Sunglasses", "Sunscreen", "Cold drinks"],
    "Cold":  ["Heaters", "Woollen clothes", "Hot beverages"],
    "Hot":   ["Cold drinks", "ACs/Fans", "Cotton clothes"],
    "Storm": ["Emergency lights", "Dry foods", "Power banks"],
}

weather = st.selectbox(
    "Select upcoming weather condition:", list(weather_products.keys())
)

if st.button("Suggest Products"):
    st.success("Based on the forecast, you should stock:")
    for item in weather_products[weather]:
        st.markdown(f"- {item}")
