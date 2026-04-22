import streamlit as st
import pandas as pd

st.title("Tech Path Analyzer 🚀")
st.markdown("### Answer the following questions to find your perfect path!")

questions = [
    {
        "q": "1. What excites you most when using a new app?",
        "options": ["A) Visual layout and design", "B) Intelligent features and data", "C) Security and privacy settings"],
        "mapping": {"A) Visual layout and design": "web", "B) Intelligent features and data": "ml", "C) Security and privacy settings": "cyber"}
    },
    {
        "q": "2. How do you prefer to solve a complex puzzle?",
        "options": ["A) Building a visible solution", "B) Finding mathematical patterns", "C) Finding hidden vulnerabilities"],
        "mapping": {"A) Building a visible solution": "web", "B) Finding mathematical patterns": "ml", "C) Finding hidden vulnerabilities": "cyber"}
    },
    {
        "q": "3. Which of these topics sounds most interesting?",
        "options": ["A) UI/UX Design", "B) Statistics and Logic", "C) Encryption and Networks"],
        "mapping": {"A) UI/UX Design": "web", "B) Statistics and Logic": "ml", "C) Encryption and Networks": "cyber"}
    },
    {
        "q": "4. What is your ultimate goal for a project?",
        "options": ["A) A fast responsive website", "B) A model that predicts future", "C) A system immune to hackers"],
        "mapping": {"A) A fast responsive website": "web", "B) A model that predicts future": "ml", "C) A system immune to hackers": "cyber"}
    },
    {
        "q": "5. How do you prefer to spend your time?",
        "options": ["A) Perfecting the interface", "B) Improving system accuracy", "C) Monitoring suspicious behavior"],
        "mapping": {"A) Perfecting the interface": "web", "B) Improving system accuracy": "ml", "C) Monitoring suspicious behavior": "cyber"}
    }
]

web_score = 0
ml_score = 0
cyber_score = 0

st.divider()

for i, item in enumerate(questions):
    with st.container(border=True):
        st.subheader(item["q"])
        choice = st.segmented_control(
            "Select your preference:",
            options=item["options"],
            key=f"q{i}"
        )
        
        if choice:
            category = item["mapping"][choice]
            if category == "web": web_score += 1
            elif category == "ml": ml_score += 1
            elif category == "cyber": cyber_score += 1

st.divider()

if st.button("Analyze My Path", use_container_width=True, type="primary"):
    st.switch_page("pages/result.py")