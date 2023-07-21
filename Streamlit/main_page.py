import streamlit as st
import time
import pandas as pd

st.title("可视化推荐")
st.divider()

output_address = st.text_input('输出地址','add your output address here')
submit_button1 = st.button('确定')

input_NL = st.text_input('您的需求','add your requirements here')
submit_button2 = st.button('提交')

input_file = st.file_uploader('文件上传',type=['csv'])
if input_file is None:
    st.stop()
df = pd.read_csv(input_file)
