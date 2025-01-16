# import library yang dibutuhkan

import os
import sys
import streamlit as st
from web_functions import load_data

# Menambahkan folder ke sys.path agar Python bisa mengimpor modul dari folder tersebut
sys.path.append(os.path.abspath('/mount/src/datamining4519/UAS_DM/Tabs'))

from Tabs import home, predict, visualise

Tabs= {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

# membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# load dataset
df, x, y = load_data()

# kondisi call app fuction
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
