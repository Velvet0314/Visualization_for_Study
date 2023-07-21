import time
import pandas as pd
import streamlit as st
from streamlit_modal import Modal

modal1 = Modal(title="", key="modal_key", max_width=2000)

if "confirm" not in st.session_state:
    st.session_state["confirm"] = False

def del_btn_click():
    st.session_state["confirm"] = True


st.title("可视化推荐")
st.divider()

output_address = st.text_input('输出地址',placeholder='add your output address here')
submit_button1 = st.button('确定',key='button1')

input_NL = st.text_input('您的需求',placeholder='add your requirements here')
submit_button2 = st.button('提交', key='button2')

input_file = st.file_uploader('文件上传',type=['csv'])
if input_file is None:
    st.stop()
df = pd.read_csv(input_file)

submit_button3 = st.button('开始生成',key='button3')
if submit_button3:
    with modal1.container():
        progress_bar = st.progress(0)
        progress = 0
        latest_iteration = st.empty()
        for i in range(100):
            time.sleep(0.02)
            progress += 1
            progress_bar.progress(progress)
            txt1 = latest_iteration.text(f'processing {i + 1}%')
        txt1.empty()
        txt1.write('success')
        time.sleep(1.5)
        modal1.close()
