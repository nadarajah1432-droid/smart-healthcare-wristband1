import streamlit as st

st.set_page_config(page_title="Project Gateway", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fafbfc; }
    h1, h3 { color: #2b5c8f; font-family: sans-serif; text-align: center; }
    .gateway-box {
        background-color: #fff0f5; 
        border: 2px solid #e0f2fe; 
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .stButton>button { background-color: #7dd3fc; color: #1e3a8a; font-weight: bold; width: 100%; border-radius: 8px; border: none; padding: 10px; }
    .stButton>button:hover { background-color: #38bdf8; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title(" Smart Healthcare Wristband Project")
st.markdown("<br>", unsafe_allow_html=True)

if 'patient_data' not in st.session_state:
    st.session_state.patient_data = {
        "name_ar": "أحمد عبد الله", "name_en": "Ahmad Abdullah",
        "age": 45,
        "disease_ar": "ارتفاع ضغط الدم وضيق التنفس المزمن", "disease_en": "Hypertension and Chronic Dyspnea",
        "relative_phone": "+967771111111", "hospital_phone": "+96701222222",
        "address_ar": "صنعاء - حي السبعين", "address_en": "Sanaa, Al Sabeen District",
        "blood_type": "O+"
    }

st.markdown("<div class='gateway-box'>", unsafe_allow_html=True)
st.subheader("🌐 Please Select System Language / الرجاء اختيار اللغة")

# زر اختيار اللغة
language = st.radio("", ["العربية (Arabic)", "English"], index=0, horizontal=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 دخول / Enter"):
    if language == "العربية (Arabic)":
        st.success("جاري الانتقال إلى الواجهة الأولى (النسخة العربية)...")
        st.switch_page("pages/arabic_portal.py")
    else:
        st.success("Switching to the 2nd Interface (English Version)...")
        st.switch_page("pages/english_portal.py")
st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("<h3 style='text-align: center; color: #2b5c8f;'>🛠️ المطورين / Creators</h3>", unsafe_allow_html=True)
if language == "العربية (Arabic)":
    with st.sidebar.expander("✨ اضغط هنا لعرض أسماء فريق العمل (أعلى اليمين)", expanded=True):
        st.markdown("""
        <div style="text-align: right; font-family: sans-serif; font-size: 15px; line-height: 1.8; color: #1e3a8a; direction: RTL;">
            <b>تم إعداد هذا المشروع بواسطة فريق التخرج:</b><br>
            💎 ندى رزقان<br>
            💎 نوال فروان<br>
            💎 البتول الزين
        </div>
        """, unsafe_allow_html=True)
else:
    with st.sidebar.expander("✨ Click to view Creators (Top Left)", expanded=True):
        st.markdown("""
        <div style="text-align: left; font-family: sans-serif; font-size: 15px; line-height: 1.8; color: #1e3a8a; direction: LTR;">
            <b>Developed by the Graduation Team:</b><br>
            💎 Nada Rezqan<br>
            💎 Nawal Farwan<br>
            💎 Al-Batoul Al-Zain
        </div>
        """, unsafe_allow_html=True)
