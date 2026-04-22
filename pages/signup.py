import streamlit as st

st.title("Create Account", anchor=False)
st.write("discover ur carrer")

with st.form("signup_form"):
    st.write("personal info")
    col1,col2=st.columns(2)
    with col1:
        name=st.text_input("full name")
        email=st.text_input("email", placeholder="example@gmail.com")
    with col2:
        age =st.number_input("age",step=1, min_value=0, max_value=90)
        password=st.text_input("password", type="password")
    col3,col4=st.columns([3,1])
    with col3:
        governement=st.text_input("Governement")

        submit=st.form_submit_button("sign up", use_container_width=True)

        if submit:
            if name and email and password and governement:
                st.session_state['name']=name
                st.session_state['age']=age
                st.session_state['email']=email
                st.session_state['governement']=f"{governement},"
                st.success(f"account created successfuly for {name}! please sign in")
                st.switch_page("pages/signin.py")
            else:
                st.error("please fill in all required feilds (name,email,password,address).")
                st.divider()
                st.write("already have an account?")
                if st.button("sign in here", use_container_width=True):
                    st.switch_page("signin.py")