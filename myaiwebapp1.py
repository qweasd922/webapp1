import streamlit as st

import google.generativeai as genai
genai.configure(api_key="AIzaSyCRm9U1jO3KfYEnrse8nTUafeI9yCy2z1g")
model = genai.GenerativeModel("gemini-pro")


text="แปลภาษา"
st.markdown(f'<p style="text-align:center;font-size:1000px">{text}</p>', unsafe_allow_html=True)
ch = st.selectbox("เลือกภาษาปลายทาง",
                 ("ไทย","อังกฤษ","เกาหลี","ญี่ปุ่น"))

text_in = st.text_input("ป้อนข้อความที่ต้องการแปล: ")

prompt = "แปลข้อความต่อไปนี้เป็นภาษา"+ ch + " " + text_in
st.text(prompt)

if st.button("แปล"):
    try:
        response = model.generate_content(prompt)
        st.text(response.text)
    except:
        st.text("no response")




    



