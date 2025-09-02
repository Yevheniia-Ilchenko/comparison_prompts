import streamlit as st

st.set_page_config(
    page_title="Prompts Analysis Tools",
    page_icon="📊",
    layout="wide"
)

st.title("Prompts Analysis Tools")
st.markdown("""
Welcome to the Prompts Analysis Tools dashboard. This application provides tools for analyzing different types of data:

1. **Email Comparison**: Compare different prompting approaches for email analysis.
2. **File Comparison**: Compare different result files from email analysis.

Please select a tool from the sidebar to get started.
""")

# Додаткова інформація про проект
st.markdown("---")
st.header("About")
st.markdown("""
This dashboard was created to help analyze and compare different approaches to processing different types of data using AI.
""")