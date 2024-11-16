import streamlit as st
from streamlit_lottie import st_lottie
import requests
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

def chat(theme):
    # Apply CSS based on the selected theme
    if theme == "Dark":
        text_color = "white"
        background_color = "#0f0f0f"  # Dark background
    else:  # Light theme
        text_color = "black"
        background_color = "white"  # Light background

    # Initialize Streamlit app
    st.markdown(f"<h1 style='color: {text_color};'>Chat with Medicare AI 🤖</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader(" ")
        st.markdown(f"<h3 style='color: {text_color};'>Engage with our intelligent medical chatbot, Medicare AI, designed to answer your healthcare-related questions. Whether you're seeking medical insights, clarifications on symptoms, or treatment recommendations, our platform ensures you receive personalized, accurate, and reliable responses.</h3>", unsafe_allow_html=True)
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medicare AI Chatbot***", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Input Your Medical Questions: Start by typing your healthcare-related question in the input field.</p>", unsafe_allow_html=True)
            st.markdown("Request a Response: After entering your question, click the `Ask` button to send it to our AI-powered chatbot.", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>View Real-Time Medical Insights: Upon submission, the chatbot generates a tailored response based on your query. The response will be displayed below the input field for immediate feedback.</p>", unsafe_allow_html=True)
            st.markdown("Explore Chat History: Review previous interactions by accessing the chat history available in the sidebar. This allows you to revisit past medical discussions.", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>Experiment and Discover: Ask various healthcare-related questions, whether about symptoms, treatment options, or general medical information. Explore the chatbot's knowledge and uncover valuable medical insights.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color};'>With these instructions, you're ready to engage with Medicare AI and receive insightful medical guidance through our conversational AI interface.</p>", unsafe_allow_html=True)

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
        "3. Review chat history in the sidebar.",
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div style='background-color: rgba(173, 133, 71, 1); padding: 10px; border-radius: 5px;'>"
        "<strong>Note:</strong><br>"
        "*Due to the current cost of API usage, you may experience limitations in output availability.<br>"
        "*We apologize for any inconvenience this may cause.<br>"
        "*Rest assured, the quality of the output is excellent when accessible."
        "</div>",
        unsafe_allow_html=True
    )

    # Main content area
    input_text = st.text_input("Enter your medical question:", key="input")
    submit_button = st.button("Ask")

    if submit_button and input_text:
        response = get_gemini_response(input_text)  # Make sure this function is defined
        st.session_state['chat_history'].append(("You", input_text))
        st.markdown(f"<h3 style='color: {text_color};'>Response:</h3>", unsafe_allow_html=True)
        for chunk in response:
            st.write(chunk.text, color=text_color)  # Note: `color` argument is not valid here
            st.session_state['chat_history'].append(("Medicare AI", chunk.text))

    # Footer
    st.markdown(f"<footer style='position: fixed; bottom: 0; width: 100%; text-align: center; background-color: {background_color}; color: {text_color}; padding: 10px;'>"
                 "<p>&copy; Powered by Medicare AI ©️ 2024</p>"
                 "</footer>", unsafe_allow_html=True)

# Call the chat function with the desired theme
# Example: chat("Light") or chat("Dark")
