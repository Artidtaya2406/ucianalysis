import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    html_1 = """
<div style="background-color:#D7BDE2;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🌷การประยุกต์ใช้งาน Machine learning"🌷</h4>

</center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

#st.title("การประยุกต์ใช้งาน Machine learning")
#st.subheader(" บนเว็บ By นางสาวอาทิตยา พันธ์นิล")
#st.subheader(" สาขาวิชาวิทยาการคอมพิวเตอร์ คณะวิทยาศาสตร์และเทคโนโลยีมหาวิทยาลัยราชภัฏนครปฐม")

lottie_url_hello = "https://lottie.host/f14ccc0b-1af9-43c6-bfed-7572d3681366/eKtdfMj042.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")
st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/1🐠Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/2🐸Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล Naive Baye", icon="2️⃣", disabled=False)
st.page_link("pages/3🐷KNNClassification.py", label="การนำเสนอข้อมูลด้วยเทคนิค KNN", icon="3️⃣", disabled=False)
st.page_link("pages/4🐱DecisionTreeClassify.py", label="การนำเสนอข้อมูลด้วยเทคนิค DecisionTree", icon="4️⃣", disabled=False)
st.page_link("pages/5🦚NaiveBayes.py", label="การนำเสนอข้อมูลด้วยเทคนิค NaiveBayes", icon="5️⃣", disabled=False)
st.page_link("pages/6🐋Regression.py", label="การนำเสนอข้อมูลด้วยเทคนิค Regression", icon="6️⃣", disabled=False)
st.page_link("https://www.kaggle.com/datasets/ananthr1/weather-prediction", label="ชุดข้อมูลสภาพอากาศ", icon="🌎")