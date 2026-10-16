import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- إعدادات الصفحة والألوان (الزهري الفاتح والأزرق الفاتح الراقية) ---
st.set_page_config(page_title="الواجهة الثانية - عربي", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #fafbfc; direction: RTL; text-align: right; }
    h1, h2, h3, h4 { color: #2b5c8f; font-family: 'Segoe UI', Tahoma, sans-serif; text-align: right; }
    .custom-container { background-color: #fff0f5; border: 2px solid #e0f2fe; padding: 25px; border-radius: 15px; margin-bottom: 20px; text-align: right; }
    .blue-card { background-color: #f0f9ff; border: 2px solid #bae6fd; padding: 25px; border-radius: 15px; margin-bottom: 20px; text-align: right; }
    .stButton>button { background-color: #7dd3fc; color: #1e3a8a; font-weight: bold; width: 100%; border-radius: 8px; }
    .stButton>button:hover { background-color: #38bdf8; color: white; }
    .status-indicator { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; }
    .bracelet-screen { background-color: #1a1f26; color: #64dfdf; padding: 25px; border-radius: 15px; font-family: monospace; text-align: right; direction: rtl; box-shadow: inset 0 0 10px rgba(0,0,0,0.5); }
    .hospital-table { width: 100%; border-collapse: collapse; background-color: white; border-radius: 8px; overflow: hidden; text-align: right; direction: RTL; }
    div[data-testid="stForm"] { text-align: right; direction: RTL; }
    [data-testid="stSidebar"] { background-color: #f0f9ff; border-left: 2px solid #e0f2fe; }
    </style>
""", unsafe_allow_html=True)

# أسماء الطالبات في أعلى جهة اليمين داخل الـ Sidebar باللغة العربية
st.sidebar.markdown("### 🛠️ معلومات فريق العمل")
with st.sidebar.expander("✨ اضغط هنا لعرض مطورات المشروع يميناً", expanded=True):
    st.markdown("""
    <div style="text-align: right; font-family: sans-serif; font-size: 15px; line-height: 1.8; color: #1e3a8a; direction: RTL;">
        <b>تم إعداد هذا المشروع بواسطة فريق التخرج:</b><br>
        💎 ندى رزقان<br>
        💎 نوال فروان<br>
        💎 البتول الزين
    </div>
    """, unsafe_allow_html=True)

if 'patient_data' not in st.session_state:
    st.switch_page("main_app.py")

p = st.session_state.patient_data
google_maps_url = "https://google.com"

st.title("👤 الواجهة الثانية: نظام الرعاية الصحي الذكي المتكامل (النسخة العربية)")

if st.button("⬅️ العودة لصفحة اختيار اللغة وبوابة الدخول"):
    st.switch_page("main_app.py")
ar_tab1, ar_tab2, ar_tab3 = st.tabs(["📋 1. لوحة تحكم المريض والأقارب", "⌚ 2. محاكي السوار الذكي", "🏥 3. واجهة استقبال المستشفى والطوارئ"])
with ar_tab1:
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
        st.markdown("### 📝 صفحة التسجيل (Configuration)")
        with st.form("ar_config_form_fixed_final_v10"):
            p["name_ar"] = st.text_input("الاسم الكامل للمريض", p["name_ar"])
            p["age"] = st.number_input("العمر", value=p["age"], min_value=1)
            p["disease_ar"] = st.text_area("التاريخ المرضي والحالة الصحية المسبقة", p["disease_ar"])
            p["relative_phone"] = st.text_input("رقم هاتف الأقارب (الطوارئ الاولى)", p["relative_phone"])
            p["hospital_phone"] = st.text_input("رقم هاتف المستشفى", p["hospital_phone"])
            p["address_ar"] = st.text_input("عنوان السكن الثابت للمريض", p["address_ar"])
            p["blood_type"] = st.text_input("فصيلة دم المريض", p["blood_type"])
            if st.form_submit_button("حفظ وتحديث الملف الطبي"):
                st.success("تم تحديث البيانات بنجاح!")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='blue-card'>", unsafe_allow_html=True)
        st.markdown("### 📊 المراقبة الحية للمؤشرات الحيوية (Live Vitals)")
        hr_val = st.number_input("ضربات القلب المستلمة حياً (BPM)", min_value=30, max_value=220, value=75, key="ar_dash_hr_final")
        ox_val = st.number_input("نسبة الأكسجين المستلمة حياً (SpO2 %)", min_value=50, max_value=100, value=98, key="ar_dash_ox_final")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if ox_val < 85 or hr_val < 45:
            st.markdown('<div class="status-indicator" style="background-color: #f8d7da; color: #842029;">🔴 دائرة حمراء وامضة: حالة حرجة جداً (تنبيه المستشفى والأقارب فوراً)</div>', unsafe_allow_html=True)
        elif ox_val < 93 or hr_val > 100:
            st.markdown('<div class="status-indicator" style="background-color: #fff3cd; color: #664d03;">🟡 دائرة صفراء: إغماء بسيط أو تشنج عارض (تم تنبيه الأقارب محلياً فقط)</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-indicator" style="background-color: #d1e7dd; color: #0f5132;">🟢 دائرة خضراء: حالة المريض مستقرة وطبيعية</div>', unsafe_allow_html=True)
            
        chart_data = pd.DataFrame({'ضربات القلب': np.random.normal(hr_val, 1, 10)})
        st.line_chart(chart_data)
        
        # خريطة قوقل ماب الحقيقية والمفهومة باللغة العربية مئة بالمئة والمنسقة
        st.markdown("<br><hr style='border-top: 1px solid #bae6fd;'><br>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #2b5c8f; text-align: right;'>📍 خريطة تتبع الموقع المباشر للمريض (Live GPS Map)</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #e0f2fe; margin-bottom: 15px; width: 100%; direction: RTL; text-align: right;">
            <span style="font-size: 16px; color: #333333; font-weight: bold; display: block; margin-bottom: 5px;">🗺️ معلومات التتبع الجغرافي النشط للسوار:</span>
            <span style="font-size: 15px; color: #555555; display: block;"><b>موقع المريض الفعلي الحالي:</b> {p['address_ar']}</span>
            <span style="font-size: 14px; color: #777777; display: block; margin-top: 3px;"><b>إحداثيات مستشعر الـ GPS الحالية:</b> خط عرض 15.326 | خط طول 44.207</span>
        </div>
        """, unsafe_allow_html=True)
        
        # تضمين خريطة Google Maps التفاعلية الحقيقية والمترجمة باللغة العربية لحي السبعين بدبوس أحمر
        google_maps_iframe_ar = '<iframe src="https://google.com" width="100%" height="360" style="border:1px solid #bae6fd; border-radius:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);" allowfullscreen="" loading="lazy"></iframe>'
        st.markdown(google_maps_iframe_ar, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="text-align: center; margin-top: 15px; width: 100%;">
            <a href="{google_maps_url}" target="_blank" style="background-color: #7dd3fc; color: #1e3a8a; padding: 12px 25px; border-radius: 8px; font-weight: bold; text-decoration: none; display: inline-block; box-shadow: 0 2px 4px rgba(0,0,0,0.05); font-size: 15px;">
                🗺️ اضغط هنا لتتبع موقع المريض حياً على شبكة خرائط Google Maps الخارجية
            </a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with ar_tab2:
    sc1, sc2 = st.columns([1, 1.2])
    with sc1:
        st.markdown("<div class='blue-container'>", unsafe_allow_html=True)
        st.markdown("#### ⚙️ متحكم القراءات ومستشعرات اللوحة (إدخال رقمي يدوي ⌨️)")
        s_hr = st.number_input("أدخل نبض القلب الفعلي للمحاكاة", min_value=30, max_value=220, value=int(hr_val), step=1, key="ar_sim_hr_manual")
        s_ox = st.number_input("أدخل نسبة الأكسجين الفعلية للمحاكاة", min_value=50, max_value=100, value=int(ox_val), step=1, key="ar_sim_ox_manual")
        fall = st.checkbox("🚨 تفعيل مستشعر السقوط أرضاً فجأة", value=(s_ox < 93), key="ar_fall_check")
        jitter = st.checkbox("🔄 تفعيل مستشعر الاهتزاز الحركي والتشنج", value=(s_hr > 100), key="ar_jitter_check")
        st.markdown("</div>", unsafe_allow_html=True)
    with sc2:
        st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
        st.markdown("#### 📱 شاشة السوار الافتراضية المدمجة (Screen Mockup)")
        if s_ox < 85 or s_hr < 45:
            st.markdown(f"""<div class="bracelet-screen" style="border-right: 5px solid red;"><h3>🚨 حالة طارئة حرجة: توقف النبض / التنفس</h3><p><b>إرشادات الإنقاذ العاجلة للمحيطين:</b></p><p>1. ابدأ بالإنعاش القلبي الرئوي (CPR): اضغط بقوة منتصف الصدر.</p><small>📡 تم إرسال الإحداثيات الجغرافية والملف الطبي للمستشفى تلقائياً.</small></div>""", unsafe_allow_html=True)
        elif fall or jitter or s_ox < 93 or s_hr > 100:
            st.markdown(f"""<div class="bracelet-screen" style="border-right: 5px solid yellow;"><h3>⚠️ تحذير: إغماء بسيط أو نوبة تشنج</h3><p>⏱️ هل أنت بخير؟ اضغط زر (أنا بخير) لإلغاء البلاغ خلال 20 ثانية لمنع إرسال البلاغ لغرفة العمليات.</p></div>""", unsafe_allow_html=True)
            if st.button("🟢 أنا بخير (إلغاء البلاغ الخاص بالأقارب)"): st.success("تم إلغاء الإنذار وتصنيف الحالة كعارض عابر.")
        else:
            st.markdown(f"""<div class="bracelet-screen" style="border-right: 6px solid #198754;"><h3>🟢 SYSTEM OK</h3><p>النبض الحقيقي: {s_hr} BPM | الأكسجين: {s_ox}%</p></div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with ar_tab3:
    st.markdown("#### 🏥 شاشة استقبال بلاغات غرف العمليات بالمستشفى")
    is_crit = (st.session_state.ar_dash_ox_final < 85) or (st.session_state.ar_dash_hr_final < 45)
    if is_crit:
        st.markdown(f"""
        <div style="background-color: #fff5f5; border-right: 6px solid red; padding: 25px; border-radius: 8px; text-align: right; direction: RTL;">
            <h2 style="color: #b02a37; margin-top:0;">🚨 بلاغ تلقائي عاجل ووارد الآن من السوار الذكي!</h2>
            <table class="hospital-table">
                <tr style="background-color: #f8f9fa;"><td style="padding:12px; width:30%;"><b>اسم المريض الكامل وعمره:</b></td><td style="padding:12px;">{p['name_ar']} ({p['age']} سنة) | فصيلة الدم: {p['blood_type']}</td></tr>
                <tr><td style="padding:12px;"><b>التاريخ والتشخيص الطبي المسبق:</b></td><td style="padding:12px;">{p['disease_ar']}</td></tr>
                <tr style="background-color: #f8f9fa;"><td style="padding:12px; color:#dc3545; font-weight:bold;"><b>المؤشرات الحيوية المستلمة حياً:</b></td><td style="padding:12px;">النبض: {st.session_state.ar_dash_hr_final} BPM | الأكسجين: {st.session_state.ar_dash_ox_final}%</td></tr>
                <tr><td style="padding:12px;"><b>رقم هاتف الأقارب للتنسيق معهم:</b></td><td style="padding:12px;">{p['relative_phone']}</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        google_maps_iframe_h_ar = '<iframe src="https://google.com" width="100%" height="400" style="border:1px solid #dc3545; border-radius:10px; box-shadow: 0 4px 10px rgba(220,53,69,0.15);" allowfullscreen="" loading="lazy"></iframe>'
        st.markdown(google_maps_iframe_h_ar, unsafe_allow_html=True)
    else:
        st.success("✅ شاشة عمليات المستشفى مستقرة تماماً ولا توجد بلاغات.")
