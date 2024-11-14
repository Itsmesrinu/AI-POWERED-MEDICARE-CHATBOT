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

def csv():
    st.header("Medical Data Analysis with CSV")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Explore Patient and Medical Data: Seamlessly analyze healthcare-related CSV datasets. Engage with AI-driven analysis to ask health-related queries, generating actionable insights and dynamic visualizations for better healthcare decisions.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medical CSV Data Analysis***")
            st.write("Upload Your CSV Files: Start by uploading your medical or patient data CSV files using the provided uploader.")
            st.write("Select Your Dataset: After uploading, choose the CSV file you want to analyze from the dropdown menu.")
            st.write("Visualize Your Data: Upon selection, the dataset will be displayed in a table. Use the interactive tools to explore and visualize key healthcare insights.")
            st.markdown("Ask Medical Queries: Use the input field to ask questions related to the patient or medical data. For example, inquire about trends like `What is the average patient age?` or `What are the recovery trends?`")
            st.write("Analyze Results: Get AI-powered insights and visualizations tailored to your query. Use the results to make informed healthcare decisions.")
            st.write("Iterate and Explore: Continue asking questions and refining your analysis to extract deeper insights from the medical data. Use AI to uncover trends, anomalies, and patterns that could aid in patient care.")
            st.write("With these instructions, you're ready to leverage AI for medical CSV data analysis. Let's explore healthcare data together!")
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
    input_text = st.text_area("Enter the medical query")
    
            # Perform analysis
    if st.button("Chat with CSV"):
                if input_text:
                    st.info("Your Query: " + input_text)
                    result = chat_with_csv(data, input_text)
    
                    # Display the result
                    if isinstance(result, str):  # Assuming result is a string response
                        st.success(result)
                    else:
                        # If the result is a plot, display it
                        plt.figure()  # Create a new figure for plotting
                        # Assuming result could be a function that generates a plot
                        # You might need to adjust this part based on your actual usage
                        result()  # Call the result if it's a plotting function
                        st.pyplot(plt.gcf())  # Display the plot


