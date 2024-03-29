from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
#from sklearn import datasets
#from sklearn import metrics

import pandas as pd
import streamlit as st

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/8aaee143-da0b-449e-997f-289e2618e341/mdCBypvI4K.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

# โหลดข้อมูล Iris
df = pd.read_csv("./data/iris.csv")
X = df.drop('variety',axis=1)
y = df['variety']

html_1 = """
<div style="background-color:#F5B7B1;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🌷การนำเสนอข้อมูลด้วยเทคนิค NaiveBayes🌷</h4></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")
# แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างและฝึกโมเดล Naive Bayes (ในกรณีของ Iris จะใช้ Gaussian Naive Bayes)
clf = GaussianNB()
clf.fit(X_train, y_train)

# ทดสอบโมเดล
#y_pred = clf.predict(X_test)

st.subheader("กรุณาป้อนข้อมูลเพื่อพยากรณ์")
spW=st.number_input('Insert sepalwidth')
spL=st.number_input('Insert sepallength')
ptW=st.number_input('Insert petalwidth')
ptL=st.number_input('Insert petallength')

if st.button("พยากรณ์"):
    x_input=[[spW,spL,ptW,ptL]] # ใส่ข้อมูลสำหรับการจำแนกข้อมูล
    y_predict2=clf.predict(x_input)
    st.write(y_predict2)
    st.button("ไม่พยากรณ์")
else:
    st.button("ไม่พยากรณ์")