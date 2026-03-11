#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:27:27 2026

@author: moloko_mokgehle
"""

import streamlit as st

# Set page configuration
st.set_page_config(page_title="Moloko Mokgehle - Portfolio", page_icon="📊", layout="wide")

# --- HEADER SECTION ---
st.title("Moloko Mokgehle")
st.write("📍 Cape Town, South Africa")
st.write("📞 +27 69 495 9634| 📧 moloko.mokgehle02@gmail.com | 🔗 [LinkedIn](https://linkedin.com/in/moloko-mokgehle)")
github_url = "https://github.com/Moloko-Mokgehle"
st.markdown(
    f"""
    <a href="{github_url}" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"
        width="30" height="30">
    </a>
    """,
    unsafe_allow_html=True
)
st.write("---")

# --- SIDEBAR SKILLS ---
st.sidebar.header("Technical Skills")
st.sidebar.subheader("Languages")
st.sidebar.code("Python, R, HTML/CSS, SQL, MATLAB, Streamlit, SAS")

st.sidebar.subheader("Tools")
st.sidebar.write("VSCode, Jupyter, Spyder, Excel, Office 365, Google Workspace, LaTeX, GitHub")

# --- EDUCATION ---
st.header("Education")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Postgraduate Diploma in Mathematical Sciences")
    st.write("Cape Peninsula University of Technology (Jan 2026 – Present)")
    st.caption("Coursework: Data Science, Machine Learning, Mathematical Modelling, Data Engineering")

with col2:
    st.subheader("Advanced Diploma in Mathematical Sciences")
    st.write("Cape Peninsula University of Technology (Jan 2021 – Dec 2025)")
    st.caption("Coursework: Statistics, Data Analysis, Algorithms, Databases, Computer Systems")

st.write("---")

# --- EXPERIENCE ---
st.header("Professional Experience")

with st.expander("Research Intern | Tamarind Hill Press (July 2024 – Dec 2024)"):
    st.write("- Conducted Qualitative literature synthesis and online research.")
    st.write("- Organized collaborative data workflows using Google Drive and Docs.")
    st.write("- Managed 20+ sources using Mendeley for accurate citations.")

with st.expander("University Application Assistant | Volunteer (Aug 2024 – Dec 2024)"):
    st.write("- Guided 50+ students through university and NSFAS applications.")
    st.write("- Built an Excel tracking system achieving 100% follow-up completion.")
    st.write("- Supported multilingual learners in diverse settings.")

st.write("---")

# --- PROJECTS ---
st.header("Projects")

# Project 1: Machine Learning
st.subheader("Student Completion Time Prediction (Machine Learning)")
st.info("Goal: Identify at-risk students using Logistic Regression, Random Forest, and XGBoost.")
st.write("**Tech Stack:** Python (Pandas, NumPy, Matplotlib, Seaborn), XGBoost")
st.write("**Methodology:** KNN Imputation, SMOTE balancing, RFE selection.")
st.write("**Results:** XGBoost achieved the highest F1-score and was selected as the final model.")
# Options for view or download the project
q01, q02, q03 = st.columns(3)
with q02:
    st.link_button("🚀 View My Project", "https://github.com/Moloko-Mokgehle/research-project-2025/blob/d486f08dd55db2ee8cba6402e216590913722f94/Mokgehle_221741143_FinalReport.pdf")
    
# Project 2: Statistical Quality Control
st.subheader("Statistical Quality Control in SA Drug Manufacturing")
st.write("- Analysed process stability with R/Excel control charts.")
st.write("- Validated data for regulatory compliance using ANOVA and Logistic Regression.")


st.write("---")
# --- DOWNLOAD BUTTON ---

b01, b02, b03 = st.columns(3)

with b02:
    try:
        with open("MokgehleMGK_CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
    
        st.download_button(
            label="📥 Download Original Resume (PDF)",
            data=PDFbyte,
            file_name="Moloko_Mokgehle_Resume.pdf",
            mime="application/octet-stream",
        )
    except FileNotFoundError:
        st.error("⚠️ Resume PDF file not found. Please ensure 'resume.pdf' is in the project folder.")
    

# --- FOOTER ---
st.write("---")
st.write("Generated via Streamlit • Moloko Mokgehle 2025")
