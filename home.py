import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/f14ccc0b-1af9-43c6-bfed-7572d3681366/eKtdfMj042.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/1🐠Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/2🐸Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล Naive Baye", icon="2️⃣", disabled=False)
st.page_link("pages/3🐷Classification.py", label="การนำเสนอข้อมูลด้วย KNN", icon="1️⃣", disabled=False)
st.page_link("https://www.kaggle.com/datasets/ananthr1/weather-prediction", label="ชุดข้อมูลสภาพอากาศ", icon="🌎")