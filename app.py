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
    st.sidebar.image(r"logomedi.png")
    navigation = st.sidebar.selectbox("Menu", ["HOME", "ABOUT", "PDF MEDICAL REPORT ANALYSIS", "PDF CONTEXT MEDICAL CHAT BOT", "CSV PATIENT DATA ANALYSIS", "MEDICAL IMAGE ANALYSIS", "CHAT WITH MEDICARE BOT"])

    if navigation == "HOME":
        home()
    elif navigation == "ABOUT":
        about()
    elif navigation == "PDF MEDICAL REPORT ANALYSIS":
        pdf()
    elif navigation == "PDF CONTEXT MEDICAL CHAT BOT":
        pdfcontextbot()
    elif navigation == "CSV PATIENT DATA ANALYSIS":
        csv()
    elif navigation == "MEDICAL IMAGE ANALYSIS":
        object_det()
    elif navigation == "CHAT WITH MEDICARE BOT":
        chat()

if __name__ == "__main__":
    main()
