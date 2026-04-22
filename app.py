
import streamlit as st
import streamlit as st


chatbot_page=st.Page(page='pages/chatbot.py', title='chat bot')
signup_page=st.Page(page='pages/signup.py', title='Sign up')
home_page=st.Page(page='pages/home.py', title='welcome to ....')
signin_page=st.Page(page='pages/signin.py', title='sign in')

# 2. Converting files to pages
home_page = st.Page(
    page='Pages/home.py',
    title='Home page',
    #icon='🏠',
    default=True
)
signin_page = st.Page(
    page='pages/signin.py', 
    title='Sign In', 
    #icon='🔑'
)
signup_page = st.Page(
    page='pages/signup.py', 
    title='Sign Up', 
    #icon='📝'
)
chatbot_page = st.Page(
    page='pages/chatbot.py', 
    title='Talk with AI', 
)

result_page=st.Page(
    page='pages/result.py', 
    title='Results'
)

survey_page=st.Page(
    page='pages/survey.py', 
    title='Survey'
)

# 3. Creating the navbar
all_pages = st.navigation(
    pages=[
        home_page, signup_page, signin_page,
        chatbot_page, survey_page, result_page
    ]
)
all_pages.run()