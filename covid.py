import streamlit as  st
import pickle
import numpy as np

def get_predicted(covid_params):
    with open("model_xgb.sav" , 'rb') as f:
        model = pickle.load(f)
    return model.predict(covid_params, validate_features=False)






st.title("CVD22:Troponin Value Prediction from COVID-19 Data")

form = st.form("My_Covid_Form")
with form:
    cols = st.columns((3, 3, 1))
    chk_mortality = cols[0].checkbox("Mortality")
    chk_copd = cols[1].checkbox("COPD")
    chk_statin= cols[2].checkbox("Statin")
    
    
    cols = st.columns((3, 3, 1))
    chk_ht = cols[0].checkbox("HT")
    chk_str = cols[1].checkbox("Steroid")

    
    cols = st.columns((3, 3, 1))
    txt_uricacide = cols[0].text_input("Uric Acide")
    txt_ckmb= cols[1].text_input("CKMB")
    txt_glu= cols[2].text_input("Glucose")
    
    cols = st.columns((3, 3, 1))
    txt_egfr = cols[0].text_input("EGFR")
    txt_basophil = cols[1].text_input("Basophil")
    txt_creatine = cols[2].text_input("Creatine")
    
    cols = st.columns((3, 3, 1))
    txt_alp = cols[0].text_input("ALP")
    txt_ddimerave = cols[1].text_input("D-Dimer Average")
    txt_ig = cols[2].text_input("Ig")
    
    cols = st.columns((3, 3, 1))
    txt_ldl = cols[0].text_input("LDL")
    txt_hdl = cols[1].text_input("HDL")
    txt_crp = cols[2].text_input("CRP")
    
    cols = st.columns((3, 3, 1))
    txt_ggt = cols[0].text_input("GGT")
    txt_lymposit = cols[1].text_input("LYMPOSIT")
    txt_fib = cols[2].text_input("Fibrogen")
    
    cols = st.columns((3, 3, 1))
    txt_fer = cols[0].text_input("Ferritin")
    txt_apttavg = cols[1].text_input("APTT Average")
    cmb_cha2ds2 = cols[2].selectbox("CHA2DS2", [0, 1 ,2, 3, 4, 5, 6, 7])
    
    cols = st.columns((1, 1, 1))
    txt_tri = cols[0].text_input("Trigliserid")
    
    submitted = st.form_submit_button("Predict")


if submitted:
    result = get_predicted([[int(chk_mortality), float(txt_ckmb), float(txt_glu), int(cmb_cha2ds2), float(txt_uricacide), float(txt_egfr), float(txt_basophil), int(chk_statin), float(txt_creatine), 
                               int(txt_alp), float(txt_ddimerave), float(txt_ig), float(txt_fer), float(txt_fib), 
                               float(txt_ggt), int(chk_ht),  int(chk_copd), float(txt_tri), 
                             float(txt_lymposit), float(txt_hdl), float(txt_ldl), int(chk_str), float(txt_apttavg), float(txt_crp)]])
try:
    
    if result[0] == 1: 
        st.success("Troponin value is above the normal value.")
    elif result[0] == 0:
        st.success("Troponin value is below the normal value.")
except:
    pass

    
     
    
    
    
    
    
    
    
    
    
    
    
    