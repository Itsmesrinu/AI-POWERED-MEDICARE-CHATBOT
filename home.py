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

def home():
    st.markdown("<h1 style='text-align: center; color: white;'>Discover the power of AI-Powered Medicare ChatBot</h1>", unsafe_allow_html=True)

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
        st.markdown('<p class="big-font bold-text">Welcome to Medicare AI</p>', unsafe_allow_html=True)
        st.subheader("Your Intelligent Healthcare Companion! 🩺🤖")
        st.write("Have questions about your medical data or reports? Need quick, accurate health insights? You're in the right place!")

    with col2:

        st.header(" ")
        st.image(r"logomedi.png")

    st.write("---")
    
    st.markdown("<h1 style='text-align: center; color: white; font-size:35px;'>Ask Medicare AI anything about your medical reports, patient data, or health-related images. From symptom analysis to contextual understanding, Medicare AI has got you covered.</h1>", unsafe_allow_html=True)
    #st.write("Simply upload your files and start chatting. Let's unlock the power of AI together! 💡")

    col3,col4,col5,col6 = st.columns(4)
    with col3:
        st.image(r"Untitled design (2).png")
    with col4:
        st.image(r"Untitled design (3).png")
    with col5:
        st.image(r"Untitled design (4).png")
    with col6:
        st.image(r"Untitled design (5).png")
    
    st.markdown("<h1 style='text-align: center; color: white; font-size:35px;'>Simply upload your medical files and start chatting with Medicare AI. Let's unlock the power of AI for healthcare! 💡</h1>", unsafe_allow_html=True)
    st.write("---")

    col7,col8 = st.columns(2)
    with col7:
        st.header("")
        st.header("Why Choose Medicare AI?")
        st.subheader("1. Instant Medical Insights: Get actionable health insights from your reports in real-time.")
        st.subheader("2. Versatile Data Analysis: Analyze CSV, medical images, or PDFs effortlessly.")
        st.subheader("3. Conversational AI: Chat with Medicare AI to explore your health data in a natural way.")
        st.subheader("4. User-Friendly: Easy-to-use interface for seamless healthcare interaction.")
        st.subheader("5. Powerful AI: Leveraging advanced AI technology for accurate medical analysis.")

    with col8:
        st.header("")
        st_lottie(l1)

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
        }
        </style>
        <div class="footer">
            Powered by Medicare AI ©️ 2024
        </div>
        """,
        unsafe_allow_html=True
    )
