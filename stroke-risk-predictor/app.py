# # import streamlit as st
# # import joblib
# # import pandas as pd

# # model = joblib.load('knn_model.pkl')
# # scaler = joblib.load('scaler.pkl')
# # expected_columns = joblib.load('columns.pkl')

# # st.title('Heart Disease Prediction by Ayu')
# # st.markdown('Please enter the following details to predict the likelihood of heart disease:')
# # age = st.slider('Age', 18, 100, 40)
# # sex = st.selectbox('Sex', ['M', 'F'])
# # chest_pain = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
# # resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200, 120)
# # cholesterol = st.number_input('Serum Cholesterol (mg/dl)', 100, 600, 200)
# # fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['1', '0'])
# # rest_ecg = st.selectbox('Resting ECG', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
# # max_hr = st.slider('Maximum Heart Rate Achieved', 60, 220, 150)
# # exercise_angina = st.selectbox('Exercise Induced Angina', ['1', '0'])
# # st_depression = st.slider('ST Depression Induced by Exercise', 0.0, 6.0, 1.0)
# # st_slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['UP', 'Flat', 'Down'])


# import streamlit as st
# import pandas as pd
# import joblib

# # Load saved model, scaler, and expected columns
# model = joblib.load("knn_model.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("columns.pkl")

# st.title("Heart Stroke Prediction by Shubham")
# st.markdown("Provide the following details to check your heart stroke risk:")

# # Collect user input
# age = st.slider("Age", 18, 100, 40)
# sex = st.selectbox("Sex", ["Male", "Female"])
# chest_pain = st.selectbox("Chest Pain Type", ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
# resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
# cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
# fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
# resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
# max_hr = st.slider("Max Heart Rate", 60, 220, 150)
# exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
# oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
# st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# # When Predict is clicked
# if st.button("Predict"):

#     # Create a raw input dictionary
#     raw_input = {
#         'Age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholesterol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex_' + sex: 1,
#         'ChestPainType_' + chest_pain: 1,
#         'RestingECG_' + resting_ecg: 1,
#         'ExerciseAngina_' + exercise_angina: 1,
#         'ST_Slope_' + st_slope: 1
#     }

#     # Create input dataframe
#     input_df = pd.DataFrame([raw_input])

#     # Fill in missing columns with 0s
#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     # Reorder columns
#     input_df = input_df[expected_columns]

#     # Scale the input
#     scaled_input = scaler.transform(input_df)

#     # Make prediction
#     prediction = model.predict(scaled_input)[0]

#     # Show result
#     if prediction == 1:
#         st.error("⚠️ High Risk of Heart Disease")
#     else:
#         st.success("✅ Low Risk of Heart Disease")
        
#         # done one basic model

import streamlit as st
import pandas as pd
import joblib

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Heart Risk Predictor",
    page_icon="🫀",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Global ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #185FA5 0%, #0C447C 100%);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    color: #E6F1FB;
}
.hero h1 { font-size: 26px; font-weight: 600; margin: 0 0 6px; }
.hero p  { font-size: 14px; opacity: 0.85; margin: 0; }
.badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border-radius: 20px;
    font-size: 11px;
    font-weight: 500;
    padding: 3px 10px;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
}

/* ── Section headings ── */
.section-head {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #888780;
    margin: 1.5rem 0 0.5rem;
}

/* ── Metric cards ── */
.metric-row { display: flex; gap: 12px; margin: 1rem 0; }
.metric-card {
    flex: 1;
    background: #F1EFE8;
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
}
.metric-val { font-size: 22px; font-weight: 600; color: #2C2C2A; }
.metric-lbl { font-size: 11px; color: #5F5E5A; margin-top: 3px; }

/* ── Result cards ── */
.result-danger {
    background: #FCEBEB;
    border: 1px solid #F09595;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-top: 1rem;
}
.result-danger h3 { color: #A32D2D; font-size: 17px; margin: 0 0 6px; }
.result-danger p  { color: #791F1F; font-size: 13px; margin: 0; }

.result-success {
    background: #EAF3DE;
    border: 1px solid #97C459;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-top: 1rem;
}
.result-success h3 { color: #3B6D11; font-size: 17px; margin: 0 0 6px; }
.result-success p  { color: #27500A; font-size: 13px; margin: 0; }

/* ── Predict button ── */
div.stButton > button {
    width: 100%;
    background: #185FA5;
    color: #E6F1FB;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 0.02em;
    margin-top: 0.75rem;
    transition: background 0.15s;
}
div.stButton > button:hover { background: #0C447C; color: white; }
div.stButton > button:active { transform: scale(0.99); }

/* ── Input tweaks ── */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] > div > div {
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Load artefacts ────────────────────────────────────────────────────────────
@st.cache_resource
def load_artefacts():
    model    = joblib.load("knn_model.pkl")
    scaler   = joblib.load("scaler.pkl")
    columns  = joblib.load("columns.pkl")
    return model, scaler, columns

model, scaler, expected_columns = load_artefacts()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">❤️ HEART HEALTH SCREENING</div>
  <h1>Stroke Risk Predictor</h1>
  <p>Enter your health metrics below to receive an instant cardiovascular risk assessment powered by a K-NN model.</p>
</div>
""", unsafe_allow_html=True)

# ── Personal information ──────────────────────────────────────────────────────
st.markdown('<div class="section-head">Personal information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 18, 100, 40, help="Your current age in years")
with col2:
    sex = st.selectbox("Sex", ["Male", "Female"])

# ── Cardiac measurements ──────────────────────────────────────────────────────
st.markdown('<div class="section-head">Cardiac measurements</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    resting_bp  = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    max_hr      = st.slider("Max Heart Rate", 60, 220, 150)
with col2:
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    oldpeak     = st.slider("Oldpeak — ST Depression", 0.0, 6.0, 1.0, step=0.1,
                            format="%.1f")

# ── Clinical indicators ───────────────────────────────────────────────────────
st.markdown('<div class="section-head">Clinical indicators</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"],
    )
with col2:
    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
    )
with col3:
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

col1, col2 = st.columns(2)
with col1:
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1],
                               format_func=lambda x: "Yes (1)" if x else "No (0)")
with col2:
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])

# ── Summary metrics ───────────────────────────────────────────────────────────
st.markdown("""
<div class="metric-row">
  <div class="metric-card">
    <div class="metric-val">{}</div>
    <div class="metric-lbl">Age</div>
  </div>
  <div class="metric-card">
    <div class="metric-val">{}</div>
    <div class="metric-lbl">BP (mm Hg)</div>
  </div>
  <div class="metric-card">
    <div class="metric-val">{}</div>
    <div class="metric-lbl">Cholesterol</div>
  </div>
  <div class="metric-card">
    <div class="metric-val">{}</div>
    <div class="metric-lbl">Max HR</div>
  </div>
</div>
""".format(age, resting_bp, cholesterol, max_hr), unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────────────────────────
if st.button("Predict my risk →"):
    raw_input = {
        "Age":        age,
        "RestingBP":  resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS":  fasting_bs,
        "MaxHR":      max_hr,
        "Oldpeak":    oldpeak,
        "Sex_"              + sex:             1,
        "ChestPainType_"    + chest_pain:      1,
        "RestingECG_"       + resting_ecg:     1,
        "ExerciseAngina_"   + exercise_angina: 1,
        "ST_Slope_"         + st_slope:        1,
    }

    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df     = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction   = model.predict(scaled_input)[0]
    probability  = model.predict_proba(scaled_input)[0]

    risk_pct = int(probability[1] * 100)

    if prediction == 1:
        st.markdown(f"""
        <div class="result-danger">
          <h3>⚠️ High risk of heart disease</h3>
          <p>Your estimated risk score is <strong>{risk_pct}%</strong>.
             Please consult a cardiologist for a comprehensive evaluation.
             This tool is a screening aid and is not a substitute for professional medical advice.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-success">
          <h3>✅ Low risk of heart disease</h3>
          <p>Your estimated risk score is <strong>{risk_pct}%</strong>.
             Keep maintaining a healthy lifestyle and schedule regular check-ups.
             This tool is a screening aid and is not a substitute for professional medical advice.</p>
        </div>
        """, unsafe_allow_html=True)

    # Probability bar
    st.markdown("#### Risk probability breakdown")
    col1, col2 = st.columns(2)
    col1.metric("Low risk probability",  f"{int(probability[0]*100)}%")
    col2.metric("High risk probability", f"{risk_pct}%",
                delta=f"{risk_pct - 50}% vs baseline",
                delta_color="inverse")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
---
<p style='text-align:center;font-size:12px;color:#888780;'>
  Built by Shubham · K-NN model · For educational purposes only
</p>
""", unsafe_allow_html=True)