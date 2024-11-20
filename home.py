import streamlit as st
import os
from streamlit_lottie import st_lottie
import requests
from pdf import pdf
from csvdata import csv
from chat import chat
from pdfcontextbot import pdfcontextbot
from object_det import object_det

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/292055de-61e6-4874-91fa-d3e60e8f22a2/gDngCr7IHX.json"

def home(theme):
    # Apply CSS based on the selected theme
    if theme == "Dark":
        text_color = "white"
        background_color = "#0f0f0f"
    else:  # Light theme
        text_color = "black"
        background_color = "white"

    st.markdown(f"<div style='background-color: {background_color}; padding: 20px;'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: {text_color};'>Discover the power of AI-Powered Medicare ChatBot</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.header("")
        st.markdown("""
        <style>
        .big-font {
            font-size:80px !important;
            color: rgba(173,133,71,255);
        }
        .small-font{
            font-size: 20px !
        }
        .bold-text{
            font-weight: bold !important;
        }
        .text-ali{
            text-align: center
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown(f'<p class="big-font bold-text" style="color: #a17739;">Welcome to Medicare AI</p>', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>Your Intelligent Healthcare Companion! 🩺🤖</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>Have questions about your medical data or reports? Need quick, accurate health insights? You're in the right place!</p>", unsafe_allow_html=True)

    with col2:
        st.header(" ")
        st.image(r"logomedi.png")

    st.write("---")
    
    st.markdown(f"<h1 style='text-align: center; color: {text_color}; font-size:35px;'>Ask Medicare AI anything about your medical reports, patient data, or health-related images. From symptom analysis to contextual understanding, Medicare AI has got you covered.</h1>", unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns(4)
    with col3:
        st.image(r"Untitled design (2).png")
    with col4:
        st.image(r"Untitled design (3).png")
    with col5:
        st.image(r"Untitled design (4).png")
    with col6:
        st.image(r"Untitled design (5).png")
    
    st.markdown(f"<h1 style='text-align: center; color: {text_color}; font-size:35px;'>Simply upload your medical files and start chatting with Medicare AI. Let's unlock the power of AI for healthcare! 💡</h1>", unsafe_allow_html=True)
    st.write("---")

    col7, col8 = st.columns(2)
    with col7:
        st.header("")
        st.markdown(f"<h3 style='color: {text_color};'>Why Choose Medicare AI?</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>1. Instant Medical Insights: Get actionable health insights from your reports in real-time.</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>2. Versatile Data Analysis: Analyze CSV, medical images, or PDFs effortlessly.</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>3. Conversational AI: Chat with Medicare AI to explore your health data in a natural way.</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>4. User-Friendly: Easy-to-use interface for seamless healthcare interaction.</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {text_color};'>5. Powerful AI: Leveraging advanced AI technology for accurate medical analysis.</h3>", unsafe_allow_html=True)
    
    with col8:
        st.header("")
        st_lottie(l1)

        # Footer
    st.markdown(f"<footer style='position: fixed; bottom: 0; width: 100%; text-align: center; background-color: {background_color}; color: {text_color}; padding: 10px;'>"
                 "<p>&copy; Powered by Medicare AI ©️ 2024</p>"
                 "</footer>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 80%;
            background-color: #000000;
            text-align: center;
            padding: 10px 0;
            color: white;
        }
        </style>
        <div class="footer">
            Powered by Medicare AI ©️ 2024
        </div>
        """,
        unsafe_allow_html=True
    )
