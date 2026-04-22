import streamlit as st  
st.title("Welcome to Trackكــ")
st.markdown("Not sure where to start? we will show you. ")

st.divider()
col1, col2 =st.columns(2)

with col1:
    with st.container(border=True):
         st.subheader("Start Trackكــ ")
         st.write('')
         if st.button("Find where you truly belong.", use_container_width=True):
            st.switch_page("pages/survey.py")
with col2:
    with st.container(border=True):
         st.subheader("AI Assistant")
         st. write("")
         if st.button("chat with AI", use_container_width=True):
            st.switch_page("pages/chatbot.py")

