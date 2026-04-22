import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Survey Results", layout="wide")

st.markdown("<h1 style='text-align: center;'>📊 Survey Graphical Results</h1>", unsafe_allow_html=True)
st.write("##")

data = {
    'Service': ['Customer Support', 'Product Quality', 'Delivery Speed', 'Price', 'Usability'],
    'Score': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)
df = df.set_index('Service') 

col1, col2, col3 = st.columns(3)
col1.metric("Total Surveys", "1,240", "+15%")
col2.metric("Average Satisfaction", "88%", "4%")
col3.metric("Response Rate", "76%", "-2%")

st.write("---")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📍 Performance Analysis (Bar Chart)")
    st.bar_chart(df)

with row1_col2:
    st.subheader("📈 Trend Visualization (Area Chart)")
    st.area_chart(df)

st.write("---")
st.subheader("📋 Raw Data Summary")

st.dataframe(df.style.highlight_max(axis=0, color='#E8DEF8'), use_container_width=True)

if st.button("Refresh Data"):
    st.rerun()