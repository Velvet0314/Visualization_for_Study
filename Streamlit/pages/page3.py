from streamlit_modal import Modal
import streamlit as st
import time
# 定义 modal
my_modal = Modal(title="", key="modal_key", max_width=2000)

# 使用 session_state 来判断 modal 里的确定按钮是否被点击
if "confirm" not in st.session_state:
    st.session_state["confirm"] = False


# 回调函数，将 session_state 置为 True
def del_btn_click():
    st.session_state["confirm"] = True

# 如果删除按钮被点击，就进行弹窗
if st.button("提交"):
    with my_modal.container():
        # 创建一个进度条
        progress_bar = st.progress(0)

        # 设置进度条的初始值为0
        progress = 0
        a = st.empty()
        a.write('loading')
        # 每隔0.1秒更新进度条的值，直到它达到100%
        while progress < 100:

            time.sleep(0.05)
            progress += 1
            progress_bar.progress(progress)
        a.empty()
        a.write('success')
        # 定义一个确定按钮，注意 key 值为指定的 session_state，on_click 调用回调函数改 session_state 的值
        st.button("确定", key="confirm", on_click=del_btn_click)

if st.session_state["confirm"]:
    st.session_state["confirm"] = False  # 恢复 session_state 为 False
    st.experimental_rerun()  # 重刷页面
