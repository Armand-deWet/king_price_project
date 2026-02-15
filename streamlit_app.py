import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from fastapi_api.src.processor import SuperheroProcessor

# Configuration & Setup
load_dotenv()
st.set_page_config(page_title="Guardian Risk Assessment", page_icon="🛡️", layout="wide")

# Custom CSS for "Production Grade" Aesthetic
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #004a99; color: white; }
    .report-card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #004a99; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# Load Shared Processor
@st.cache_resource
def get_processor():
    return SuperheroProcessor()

processor = get_processor()

# Sidebar - Input Parameters
st.sidebar.header("📋 Applicant Profile")
st.sidebar.markdown("Enter the hero's details to calculate risk.")

age = st.sidebar.slider("Hero Age", 18, 100, int(os.getenv("MEAN_AGE", 35)))
credit_score = st.sidebar.number_input("Credit Score", 1, 850, 650)
property_count = st.sidebar.slider("Properties Owned", 0, 100, 1)
teleportation = st.sidebar.checkbox("Has Teleportation Power?")

# Main UI
st.title("🛡️ Guardian Insurance: Risk Rating Engine")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Predictive Risk Assessment")
    st.write("Estimating annual public destruction events based on fiscal and physical profiles.")
    
    # Prediction
    if st.button("Generate Risk Quote"):
        # We use the processor's logic directly. 
        input_data = pd.DataFrame([{
            "property_count": property_count,
            "age": age,
            "credit_score": credit_score,
            "power_teleportation": 1 if teleportation else 0
        }])
        
        # Use the model and features loaded by the processor
        X = input_data[processor.required_features]
        prediction = processor.model.predict(X)[0]
        final_val = int(max(0, round(prediction)))
        
        # Display Results
        st.markdown(f"""
            <div class="report-card">
                <h3>Estimated Annual Destruction Events</h3>
                <h1 style='color: #d9534f;'>{final_val}</h1>
                <p><b>Risk Tier:</b> {"High Risk" if final_val > 5 else "Standard" if final_val > 1 else "Low Risk"}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.info("Basis of Quote: Weighted primarily by Property Count and Credit Score.")

with col2:
    st.image("https://img.icons8.com/fluency/240/shield.png", width=150)
    st.markdown("""
        **Policy Guidelines:**
        - Destruction > 5 = Manual Underwriting.
        - Teleportation = Automatic Surcharge.
        - Source: S.H.I.E.L.D. Verified.
    """)