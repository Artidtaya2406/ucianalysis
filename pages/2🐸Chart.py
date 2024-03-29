import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/09307672-f116-47b0-95b6-5b0d518c907d/17pfXgaSVf.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")


#st.title("💡Website Developing using Python💡")
#st.header("💡 Website Developing using Python 💡")

#st.subheader("✨💛 Artidtaya Pannin 💛✨")


dt=pd.read_csv('./data/seattle-weather.csv')

#st.subheader("ข้อมูลสภาพอากาศ Weather")
#st.write(dt.head(10))
#Index(['precipitation', 'temp_max', 'temp_min', 'wind',
#       'variety'],

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>✨💛 กราฟแสดงข้อมูลสภาพอากาศ 💛✨</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


#st.subheader("สถิติข้อมูลสภาพอากาศ Weather")

st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['precipitation'].sum())
cl2.write(dt['temp_max'].sum())
cl3.write(dt['temp_min'].sum())
cl4.write(dt['wind'].sum())
import numpy as np
import matplotlib.pyplot as plt
labels = ['precipitation','temp_max', 'temp_min','wind']
sizes = [35,25,15,25]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)



st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['precipitation'].mean())
cl12.write(dt['temp_max'].mean())
cl13.write(dt['temp_min'].mean())
cl14.write(dt['wind'].mean())
st.write("กราฟแท่ง")
a=dt['precipitation'].sum()
b=dt['temp_max'].sum()
c=dt['temp_min'].sum()
d=dt['wind'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["precipitation", "temp_max", "temp_min","wind"])
st.bar_chart(cx)


st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['precipitation'].max())
cl22.write(dt['temp_max'].max())
cl23.write(dt['temp_min'].max())
cl24.write(dt['wind'].max())
st.write("กราฟแท่ง")
a=dt['precipitation'].sum()
b=dt['temp_max'].sum()
c=dt['temp_min'].sum()
d=dt['wind'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["precipitation", "temp_max", "temp_min","wind"])
st.bar_chart(cx)

#import numpy as np
#import matplotlib.pyplot as plt
#labels = ['precipitation','temp_max', 'temp_min','wind']
#sizes = [35,25,15,25]
#explode = (0, 0.1,0,0) 
#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
#st.pyplot(fig1)


st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['precipitation'].min())
cl32.write(dt['temp_max'].min())
cl33.write(dt['temp_min'].min())
cl34.write(dt['wind'].min())

st.write("กราฟแท่ง")
a=dt['precipitation'].sum()
b=dt['temp_max'].sum()
c=dt['temp_min'].sum()
d=dt['wind'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["precipitation", "temp_max", "temp_min","wind"])
st.bar_chart(cx)