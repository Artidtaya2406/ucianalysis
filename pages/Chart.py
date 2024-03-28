import streamlit as st
import pandas as pd

#st.title("💡Website Developing using Python💡")
#st.header("💡 Website Developing using Python 💡")

st.subheader("✨💛 Artidtaya Pannin 💛✨")


dt=pd.read_csv('./data/seattle-weather.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))
#Index(['precipitation', 'temp_max', 'temp_min', 'wind',
#       'variety'],

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['precipitation'].sum())
cl2.write(dt['temp_max'].sum())
cl3.write(dt['temp_min'].sum())
cl4.write(dt['wind'].sum())


st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['precipitation'].mean())
cl12.write(dt['temp_max'].mean())
cl13.write(dt['temp_min'].mean())
cl14.write(dt['wind'].mean())


st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['precipitation'].max())
cl22.write(dt['temp_max'].max())
cl23.write(dt['temp_min'].max())
cl24.write(dt['wind'].max())

import numpy as np
import matplotlib.pyplot as plt
labels = ['Men', 'Women','','']
sizes = [35,25,15,25]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)


st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['precipitation'].min())
cl32.write(dt['temp_max'].min())
cl33.write(dt['temp_min'].min())
cl34.write(dt['wind'].min())

st.write("Line_Chart")
cc=[3,8,1,10]
st.line_chart(cc)