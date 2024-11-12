import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os
import google.generativeai as genai

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/3dffcec0-9580-4675-be95-ddd7e09834a7/YMQN5pO39Q.json"

# Configure Google API
GOOGLE_API_KEY = "API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

def chat():
    # Function to load Gemini Pro model and get responses
    model = genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])

    def get_gemini_response(question):
        response = chat.send_message(question, stream=True)
        return response

    # Initialize Streamlit app
    st.title("Chat with Medicare AI 🤖")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Engage with our intelligent medical chatbot, Medicare AI, designed to answer your healthcare-related questions. Whether you're seeking medical insights, clarifications on symptoms, or treatment recommendations, our platform ensures you receive personalized, accurate, and reliable responses.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medicare AI Chatbot***")
            st.write("Input Your Medical Questions: Start by typing your healthcare-related question in the input field.")
            st.markdown("Request a Response: After entering your question, click the `Ask` button to send it to our AI-powered chatbot.")
            st.write("View Real-Time Medical Insights: Upon submission, the chatbot generates a tailored response based on your query. The response will be displayed below the input field for immediate feedback.")
            st.markdown("Explore Chat History: Review previous interactions by accessing the chat history available in the sidebar. This allows you to revisit past medical discussions.")
            st.write("Experiment and Discover: Ask various healthcare-related questions, whether about symptoms, treatment options, or general medical information. Explore the chatbot's knowledge and uncover valuable medical insights.")
            st.write("With these instructions, you're ready to engage with Medicare AI and receive insightful medical guidance through our conversational AI interface.")

    with col2:
        st_lottie(l1)

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Sidebar
    st.sidebar.title("Instructions")
    st.sidebar.markdown(
        "1. Input your medical question in the text box below.\n"
        "2. Click the 'Ask' button to receive a response.\n"
        "3. Review chat history in the sidebar."
    )

    # Main content area
    input_text = st.text_input("Enter your medical question:", key="input")
    submit_button = st.button("Ask")

    if submit_button and input_text:
        response = get_gemini_response(input_text)
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Medicare AI", chunk.text))

    # # Chat history
    # st.sidebar.title("Chat History")
    # chat_history = st.sidebar.empty()
    # for role, text in st.session_state['chat_history']:
    #     chat_history.write(f"**{role}:** {text}")

    # Apply some styling
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
            }
            .sidebar .sidebar-content .block-container {
                padding: 0px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
