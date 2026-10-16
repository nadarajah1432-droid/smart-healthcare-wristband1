import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- إعدادات الصفحة والألوان (الزهري الفاتح والأزرق الفاتح الراقية) ---
st.set_page_config(page_title="2nd Interface - English Version", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #fafbfc; direction: LTR; text-align: left; }
    h1, h2, h3, h4 { color: #2b5c8f; font-family: 'Segoe UI', Tahoma, sans-serif; font-weight: 600; text-align: left; }
    .custom-container { background-color: #fff0f5; border: 2px solid #e0f2fe; padding: 25px; border-radius: 15px; margin-bottom: 20px; text-align: left; }
    .blue-container { background-color: #f0f9ff; border: 2px solid #bae6fd; padding: 25px; border-radius: 15px; margin-bottom: 20px; text-align: left; }
    .stButton>button { background-color: #7dd3fc; color: #1e3a8a; font-weight: bold; width: 100%; border-radius: 8px; }
    .stButton>button:hover { background-color: #38bdf8; color: white; }
    .status-indicator { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; }
    .bracelet-screen { background-color: #1a1f26; color: #64dfdf; padding: 25px; border-radius: 15px; font-family: monospace; text-align: left; box-shadow: inset 0 0 15px rgba(0,0,0,0.5); border-left: 5px solid #64dfdf; }
    .sms-box { background-color: #e9ecef; border-left: 5px solid #6c757d; padding: 15px; border-radius: 8px; color: #333; text-align: left; }
    .hospital-table { width: 100%; border-collapse: collapse; background-color: white; border-radius: 8px; overflow: hidden; text-align: left; direction: LTR; }
    [data-testid="stSidebar"] { background-color: #f0f9ff; border-right: 2px solid #e0f2fe; }
    div[data-testid="stForm"] { text-align: left; direction: LTR; }
    </style>
""", unsafe_allow_html=True)

# أسماء الطالبات في أعلى جهة اليسار داخل الـ Sidebar باللغة الإنجليزية
st.sidebar.markdown("### 🛠️ Project Developers Info")
with st.sidebar.expander("✨ Click to view Creators", expanded=True):
    st.markdown("""
    <div style="text-align: left; font-family: sans-serif; font-size: 15px; line-height: 1.8; color: #1e3a8a; direction: LTR;">
        <b>Developed by the Graduation Team:</b><br>
        💎 Nada Rezqan<br>
        💎 Nawal Farwan<br>
        💎 Al-Batoul Al-Zain
    </div>
    """, unsafe_allow_html=True)

if 'patient_data' not in st.session_state:
    st.switch_page("main_app.py")

p = st.session_state.patient_data
google_maps_url = "https://google.com"

st.title("👤 2nd Interface: Patient & Relative Portal (English Version)")

if st.button("⬅️ Back to Language Selection Portal"):
    st.switch_page("main_app.py")
en_tab1, en_tab2, en_tab3 = st.tabs(["📋 1. Patient & Relative Dashboard", "⌚ 2. Smart Wristband Simulator", "🏥 3. Hospital Emergency Portal"])
with en_tab1:
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
        st.markdown("#### 📝 Configuration Profile (EEPROM Data)")
        with st.form("en_config_form_final_v10"):
            name = st.text_input("Name", p["name_en"])
            age = st.number_input("Age", value=p["age"], min_value=1)
            disease = st.text_area("Medical History", p["disease_en"])
            relative_phone = st.text_input("Relative Phone", p["relative_phone"])
            hospital_phone = st.text_input("Hospital Phone", p["hospital_phone"])
            address = st.text_input("Address", p["address_en"])
            if st.form_submit_button("Save & Update Profile"):
                st.success("Profile saved successfully!")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='custom-container' style='background-color: #f0f9ff;'>", unsafe_allow_html=True)
        st.markdown("#### 📊 Live Vitals Stream Remote Monitoring")
        
        hr_val = st.number_input("Enter Heart Rate (BPM)", min_value=30, max_value=220, value=75, step=1, key="en_hr_manual_fix")
        ox_val = st.number_input("Enter Blood Oxygen (SpO2 %)", min_value=50, max_value=100, value=98, step=1, key="en_ox_manual_fix")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if ox_val < 85 or hr_val < 45:
            st.markdown('<div class="status-indicator" style="background-color: #f8d7da; color: #842029;">🔴 Flashing Red: Critical Condition (Hospital notified immediately)</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-indicator" style="background-color: #d1e7dd; color: #0f5132;">🟢 Green Indicator: Vitals Stable</div>', unsafe_allow_html=True)
            
        chart_data = pd.DataFrame({'Heart Rate': np.random.normal(hr_val, 1, 10)})
        st.line_chart(chart_data)
        
        # خريطة قوقل ماب الحقيقية والمفهومة باللغة الإنجليزية للواجهة الأجنبية
        st.markdown("#### 📍 Interactive GPS Map Tracking Status (Google Maps Live)")
        st.markdown(f'<p style="font-size:15px;"><b>Patient Current Address:</b> {p["address_en"]}</p>', unsafe_allow_html=True)
        
        google_maps_iframe_en = '<iframe src="https://google.com" width="100%" height="340" style="border:1px solid #bae6fd; border-radius:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);" allowfullscreen="" loading="lazy"></iframe>'
        st.markdown(google_maps_iframe_en, unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:8px;"><a href="{google_maps_url}" target="_blank" style="color: #0284c7; font-weight: bold; text-decoration: underline;">Open Location on official Google Maps</a></p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with en_tab2:
    sc1, sc2 = st.columns([1, 1.2])
    with sc1:
        st.markdown("<div class='blue-container'>", unsafe_allow_html=True)
        st.markdown("#### ⚙️ Manual Sensor Inputs (No Sliders ⌨️)")
        s_hr = st.number_input("Input Simulated Heart Rate for Testing", min_value=30, max_value=220, value=int(hr_val), step=1, key="en_sim_hr_num_manual_fix")
        s_ox = st.number_input("Input Simulated Oxygen level for Testing", min_value=50, max_value=100, value=int(ox_val), step=1, key="en_sim_ox_num_manual_fix")
        fall = st.checkbox("🚨 Trigger Fall Sensor Impact", key="en_fall_manual_fix")
        jitter = st.checkbox("🔄 Trigger Convulsion Motion Jitter", key="en_jitter_manual_fix")
        st.markdown("</div>", unsafe_allow_html=True)
    with sc2:
        st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
        st.markdown("#### 📱 Smart Wristband Screen Mockup")
        if s_ox < 85 or s_hr < 45:
            st.markdown("""<div class="bracelet-screen" style="border-left: 5px solid #dc3545;"><h3>🚨 ALERT: CRITICAL CRISIS DETECTED</h3><p>First-Aid Guide: Begin chest compressions (CPR).</p></div>""", unsafe_allow_html=True)
        elif fall or jitter or s_ox < 93 or s_hr > 100:
            st.markdown("""<div class="bracelet-screen" style="border-left: 5px solid #ffc107;"><h3>⚠️ WARNING: FAINTING DETECTED</h3><p>Countdown: 20 seconds. Press button below to cancel.</p></div>""", unsafe_allow_html=True)
            if st.button("Cancel Alert"): st.success("Alert successfully dismissed!")
        else:
            st.markdown("""<div class="bracelet-screen" style="border-left: 5px solid #198754;"><h3>🟢 SYSTEM STATUS: OK</h3><p>Pulse: {s_hr} BPM | Oxygen: {s_ox}%</p></div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with en_tab3:
    st.markdown("#### 🏥 Hospital Emergency Operations Portal")
    is_crit = (st.session_state.en_hr_manual_fix < 45) or (st.session_state.en_ox_manual_fix < 85)
    if is_crit:
        st.markdown(f"""
        <div style="background-color: #fff5f5; border-left: 6px solid #dc3545; padding: 25px; border-radius: 8px;">
            <h2 style="color: #b02a37; margin-top:0;">🚨 AUTOMATED CRITICAL EMERGENCY TELEMETRY RECEIVED</h2>
            <table class="hospital-table" style="width:100%; font-size:15px;">
                <tr style="background-color: #f8f9fa;"><td style="padding:12px; width:30%;"><b>Patient Name & Age:</b></td><td style="padding:12px;">{p['name_en']} (Age: {p['age']} yrs) | Blood Type: {p['blood_type']}</td></tr>
                <tr><td style="padding:12px;"><b>Vitals at Crash Event:</b></td><td style="padding:12px; color:#dc3545; font-weight:bold;">Pulse: {st.session_state.en_hr_manual_fix} BPM | SpO2: {st.session_state.en_ox_manual_fix}%</td></tr>
                <tr style="background-color: #f8f9fa;"><td style="padding:12px;"><b>📍 Ambulance Route (Live GPS Link):</b></td><td style="padding:12px;"><a href="https://google.com" target="_blank" style="color:#0d6efd; font-weight:bold; text-decoration: underline;">Click here to open Google Maps directly</a></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        google_maps_iframe_h_en = '<iframe src="https://google.com" width="100%" height="400" style="border:0; border-radius:10px; box-shadow: 0 4px 10px rgba(220,53,69,0.15);" allowfullscreen="" loading="lazy"></iframe>'
        st.markdown(google_maps_iframe_h_en, unsafe_allow_html=True)
    else:
        st.success("Answering lines clean. Hospital Emergency Portal is clear.")
