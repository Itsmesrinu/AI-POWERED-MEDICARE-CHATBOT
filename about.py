import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/913b6a51-e61d-45c6-b2fb-80723fe7171f/NzKkcY1mUv.json"
l2 = "https://lottie.host/2faac3d2-56d8-4471-8df1-bb56bf6fb799/ff9lxre1nU.json"
l3 = "https://lottie.host/11d7731c-f8f7-45ff-89d7-c7c11d980efd/ilMGdhHEoe.json"
l4 = "https://lottie.host/ca361236-4c82-4523-927a-69683924fe33/Udz13lEk8r.json"
l5 = "https://lottie.host/05b244e7-3c08-4440-b3d1-9c3d656cada0/uZ4x2KXm1v.json"
l6 = "https://lottie.host/6802bb15-0d2e-4b0a-af28-32c0b8c4c31a/TKMi9L7zkK.json"
l7 = "https://lottie.host/4f47e133-f8b8-4eab-bd9e-b4ee759f90ea/ZWkQwQyPsW.json"
l8 = "https://lottie.host/33f81951-c5a3-4a57-a9f2-cbdd81fa8119/pdDzXH4HdU.json"

def about(theme):
    # Apply CSS based on the selected theme
    if theme == "Dark":
        text_color = "white"
        background_color = "#0f0f0f"  # Dark background
    else:  # Light theme
        text_color = "black"
        background_color = "white"  # Light background

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h1 style='color: {text_color};'>Know About Us!!</h1>", unsafe_allow_html=True)
        st.header(" ")
        st.header(" ")
        st.markdown(f"<h3 style='color: {text_color};'>Welcome to AI-Powered Medicare ChatBot, an innovative platform that harnesses AI to revolutionize healthcare data analysis and interaction. Our project combines cutting-edge technologies to deliver seamless experiences in analyzing medical PDFs, CSV-based health data, and diagnostic imagery while engaging in natural language conversations.</h3>", unsafe_allow_html=True)
    with col2:
        st_lottie(l1)
    
    st.write("---")
    
    col3, col4 = st.columns(2)
    with col3:
        st_lottie(l2)
    with col4:
        
        st.markdown(f"<h1 style='color: {text_color};'>Our Mission</h1>", unsafe_allow_html=True)
        st.header(" ")
        st.header(" ")
        st.markdown(f"<h3 style='color: {text_color};'>Empowering healthcare professionals and patients with innovative AI technologies to unlock valuable medical insights effortlessly and efficiently. We strive to:</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>- **Empower**: Provide tools to enable healthcare professionals to make informed decisions based on data insights.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>- **Innovate**: Push the boundaries of AI and healthcare data analysis to deliver impactful solutions.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>- **Simplify**: Make advanced healthcare technologies accessible and user-friendly for all.</p>", unsafe_allow_html=True)

    st.write("---")
    
    col9, col10 = st.columns(2)
    with col9:
        st.markdown(f"<h1 style='color: {text_color};'>Our Commitment to Excellence</h1>", unsafe_allow_html=True)
        st.header(" ")
        st.header(" ")
        st.markdown(f"<h3 style='color: {text_color};'>At AI-Powered Medicare ChatBot, we are committed to delivering excellence in healthcare innovation. Our solutions integrate advanced AI technologies with intuitive user interfaces to ensure seamless experiences for all users.</h3>", unsafe_allow_html=True)
    with col10:
        st_lottie(l7)

    st.write("---")
    
    col11, col12 = st.columns(2)
    with col11:
        st_lottie(l8)
    with col12:
        st.markdown(f"<h1 style='color: {text_color};'>Data-Driven Healthcare Innovation</h1>", unsafe_allow_html=True)
        st.header(" ")
        st.header(" ")
        st.markdown(f"<h3 style='color: {text_color};'>We believe in leveraging the power of AI to drive innovation in healthcare. Our platform empowers healthcare professionals to explore insights, make informed decisions, and unlock new opportunities for growth in the medical domain.</h3>", unsafe_allow_html=True)

    st.write("---")
    
    st.markdown(f"<h1 style='color: {text_color};'>Explore Our Advanced Features</h1>", unsafe_allow_html=True)
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st_lottie(l3)
        st.markdown(f"<h3 style='color: {text_color};'>PDF Medical Report Analysis</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>Analyze medical PDF documents with precision. Extract actionable insights from clinical notes and diagnostic reports using AI-powered tools.</p>", unsafe_allow_html=True)

    with col6:
        st_lottie(l4)
        st.markdown(f"<h3 style='color: {text_color};'>CSV Health Data Analysis</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>Visualize and analyze structured health datasets. Pose natural language queries and receive instant insights and visualizations tailored to healthcare.</p>", unsafe_allow_html=True)

    with col7:
        st_lottie(l5)
        st.markdown(f"<h3 style='color: {text_color};'>Medical Image Analysis</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>Leverage advanced object detection and image processing models to analyze diagnostic imagery and extract valuable insights.</p>", unsafe_allow_html=True)

    with col8:
        st_lottie(l6)
        st.markdown(f"<h3 style='color: {text_color};'>AI-Powered Chatbot</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>Engage in natural language conversations with our AI-powered chatbot to receive personalized healthcare advice and support.</p>", unsafe_allow_html=True)
    # Footer
    st.markdown(f"<footer style='position: fixed; bottom: 0; width: 100%; text-align: center; background-color: {background_color}; color: {text_color}; padding: 10px;'>"
                 "<p>&copy; Powered by Medicare AI ©️ 2024</p>"
                 "</footer>", unsafe_allow_html=True)
