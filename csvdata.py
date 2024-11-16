import streamlit as st
from streamlit_lottie import st_lottie
from pandasai.llm.openai import OpenAI
import requests
import os
import pandas as pd
from pandasai import SmartDataframe
import matplotlib

# Use a non-interactive backend
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/2f7cf9a0-3475-430c-87c7-1664b5e17660/GUdpy07yaC.json"

openai_api_key = "API KEY"

def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    return result

def csv(theme):
    # Apply CSS based on the selected theme
    if theme == "Dark":
        text_color = "white"
        background_color = "#0f0f0f"  # Dark background
    else:  # Light theme
        text_color = "black"
        background_color = "white"  # Light background

    st.markdown(f"<h1 style='color: {text_color};'>Medical Data Analysis with CSV</h1>", unsafe_allow_html=True)

    st.sidebar.title("Instructions")
    st.sidebar.markdown(f"<p style='color: {text_color};'>1. Upload your CSV medical file.</p>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<p style='color: {text_color};'>2. Click the `Submit & Process` button.</p>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<p style='color: {text_color};'>3. Type your question exactly what you want about the CSV file.</p>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<p style='color: {text_color};'>4. Get insights from the AI chatbot.</p>", unsafe_allow_html=True)

    # Highlighted note under instructions
    st.sidebar.markdown(
        "<div style='background-color: rgba(173, 133, 71, 1); padding: 10px; border-radius: 5px;'>"
        "<strong>Note:</strong><br>"
        "*Due to the current cost of API usage, you may experience limitations in output availability.<br>"
        "*We apologize for any inconvenience this may cause.<br>"
        "*Rest assured, the quality of the output is excellent when accessible."
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.markdown(f"<h3 style='color: {text_color};'>Explore Patient and Medical Data: Seamlessly analyze healthcare-related CSV datasets. Engage with AI-driven analysis to ask health-related queries, generating actionable insights and dynamic visualizations for better healthcare decisions.</h3>", unsafe_allow_html=True)

        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medical CSV Data Analysis***", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Upload Your CSV Files: Start by uploading your medical or patient data CSV files using the provided uploader.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Select Your Dataset: After uploading, choose the CSV file you want to analyze from the dropdown menu.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Visualize Your Data: Upon selection, the dataset will be displayed in a table. Use the interactive tools to explore and visualize key healthcare insights.</p>", unsafe_allow_html=True)
            st.markdown("Ask Medical Queries: Use the input field to ask questions related to the patient or medical data. For example, inquire about trends like `What is the average patient age?` or `What are the recovery trends?`", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Analyze Results: Get AI-powered insights and visualizations tailored to your query. Use the results to make informed healthcare decisions.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Iterate and Explore: Continue asking questions and refining your analysis to extract deeper insights from the medical data. Use AI to uncover trends, anomalies, and patterns that could aid in patient care.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>With these instructions, you're ready to leverage AI for medical CSV data analysis. Let's explore healthcare data together!</p>", unsafe_allow_html=True)

        # Upload multiple CSV files
        input_csvs = st.file_uploader("Upload your Medical CSV files", type=['csv'], accept_multiple_files=True)

        if input_csvs:
            # Select a CSV file from the uploaded files using a dropdown menu
            selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
            selected_index = [file.name for file in input_csvs].index(selected_file)

            # Load and display the selected CSV file 
            st.info("CSV uploaded successfully")
            data = pd.read_csv(input_csvs[selected_index])
            st.dataframe(data, use_container_width=True)

    with col2:
        st_lottie(l1)

    # Enter the query for analysis
    st.info("Chat Below")
    input_text = st.text_area("Enter the medical query", key="query")

    # Perform analysis
    if st.button("Chat with CSV"):
        if input_text:
            st.info("Your Query: " + input_text)
            result = chat_with_csv(data, input_text)

            # Display the result
            if isinstance(result, str):  # Assuming result is a string response
                st.success(result)
            else:
                # Handle the case where result is not a string
                st.error("Unexpected result format.")

    # Footer
    st.markdown(f"<footer style='position: fixed; bottom: 0; width: 100%; text-align: center; background-color: {background_color}; color: {text_color}; padding: 10px;'>"
                 "<p>&copy; Powered by Medicare AI ©️ 2024</p>"
                 "</footer>", unsafe_allow_html=True)

    # Apply some styling
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the csv function with the desired theme
# Example: csv("Light") or csv("Dark")
