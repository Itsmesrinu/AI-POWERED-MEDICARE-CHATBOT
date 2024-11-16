import streamlit as st
import streamlit_option_menu as option_menu
import os
from home import home
from about import about
from pdf import pdf
from csvdata import csv
from chat import chat
from pdfcontextbot import pdfcontextbot
from object_det import object_det

def main():
    st.set_page_config(layout='wide')
    # Theme selection
    theme = st.sidebar.radio("Select Theme [Prefer Dark Theme here and CLick : at the top right -> Settings -> Dark  or Both use white]", ("Dark", "Light"))

    # Apply CSS based on the selected theme
    if theme == "Dark":
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #1e1e1e; /* Dark background */
                color: white; /* White text */
            }
            .sidebar .sidebar-content {
                background-color: #2b2b2b; /* Dark sidebar */
                color: white; /* White text in sidebar */
            }
            .sidebar .sidebar-header {
                background-color: #2b2b2b; /* Dark sidebar header */
                color: white; /* White text in sidebar header */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:  # Light theme
        st.markdown(
            """
            <style>
            .stApp {
                background-color: white; /* Light background */
                color: black; /* Black text */
            }
            .sidebar .sidebar-content {
                background-color: #f0f0f0; /* Light sidebar */
                color: black; /* Black text in sidebar */
            }
            .sidebar .sidebar-header {
                background-color: #f0f0f0; /* Light sidebar header */
                color: black; /* Black text in sidebar header */
            }
            </style>
            """,
            unsafe_allow_html=True
        )


    st.sidebar.image(r"logomedi.png")
    navigation = st.sidebar.selectbox("Menu", ["HOME", "ABOUT", "PDF MEDICAL REPORT ANALYSIS", "PDF CONTEXT MEDICAL CHAT BOT", "CSV PATIENT DATA ANALYSIS", "MEDICAL IMAGE ANALYSIS", "CHAT WITH MEDICARE BOT"])

    if navigation == "HOME":
        home(theme)
    elif navigation == "ABOUT":
        about(theme)
    elif navigation == "PDF MEDICAL REPORT ANALYSIS":
        pdf(theme)
    elif navigation == "PDF CONTEXT MEDICAL CHAT BOT":
        pdfcontextbot(theme)
    elif navigation == "CSV PATIENT DATA ANALYSIS":
        csv(theme)
    elif navigation == "MEDICAL IMAGE ANALYSIS":
        object_det(theme)
    elif navigation == "CHAT WITH MEDICARE BOT":
        chat(theme)

if __name__ == "__main__":
    main()
