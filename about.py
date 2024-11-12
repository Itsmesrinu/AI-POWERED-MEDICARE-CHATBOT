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

def about():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Know About Us!!")
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.subheader("Welcome to AI-Powered Medicare ChatBot, a revolutionary platform that leverages AI to provide real-time medical insights and healthcare assistance. Our project combines cutting-edge AI technologies to analyze medical reports, patient data, and health-related images, while engaging users in intelligent conversations about their health and medical needs.")
    with col2:
        st_lottie(l1)
    st.write("---")
    
    col3, col4 = st.columns(2)
    with col3:
        st_lottie(l2)
    with col4:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Our Mission")
        st.subheader("Empowering individuals and healthcare providers with innovative AI-driven tools to unlock valuable insights from medical data effortlessly and securely. Our goal is to enhance patient care by delivering cutting-edge healthcare solutions through AI.")
        st.markdown("- **Empower**: Empower patients and healthcare professionals with the tools and insights needed for informed medical decisions.")
        st.markdown("- **Innovate**: Push the boundaries of healthcare technology by leveraging the latest advancements in AI and medical data analysis.")
        st.markdown("- **Simplify**: Simplify healthcare data analysis and interaction, making advanced AI technologies accessible and easy-to-use for everyone.")

    st.write("---")
    
    col9, col10 = st.columns(2)
    with col9:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Our Commitment to Healthcare Excellence")
        st.subheader("At Medicare AI, we are dedicated to delivering excellence in healthcare services through AI. Our platform combines cutting-edge AI technologies with intuitive user interfaces to provide a seamless experience in medical data analysis and patient care.")
    with col10:
        st_lottie(l7)
    
    st.write("---")
    
    col11, col12 = st.columns(2)
    with col11:
        st_lottie(l8)
    with col12:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Data-driven Medical Innovation")
        st.subheader("We believe in the power of data to drive healthcare innovation. Our platform empowers individuals and healthcare providers to unlock the full potential of their medical data, enabling better patient outcomes and more informed decision-making.")

    # Add footer with CSS for fixed positioning
    st.write("---")
    st.title("Explore Our Advanced Healthcare Features")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st_lottie(l3)
        st.write("PDF Medical Report Analysis")
        st.write("Analyze PDF medical reports with precision. Engage with an AI-powered chatbot to extract actionable insights and knowledge from health data effortlessly.") 

    with col6:
        st_lottie(l4)
        st.write("CSV Patient Data Analysis")
        st.write("Visualize and analyze patient data from CSV files with ease. Pose natural language queries for patient data exploration and receive instant medical insights.")

    with col7:
        st_lottie(l5)
        st.write("Medical Image Analysis")
        st.write("Utilize advanced object detection algorithms for medical images. Accurately identify objects within images to assist in diagnosis and analysis.")

    with col8:
        st_lottie(l6)
        st.write("Conversational Medical AI")
        st.write("Engage in insightful medical conversations powered by AI. Receive intelligent responses tailored to your health inquiries and improve patient care through AI.")

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

