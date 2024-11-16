import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplate import css, bot_template, user_template

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/dfa2260c-7c80-4671-8bb5-fd853f9c5f37/81mapnwT5f.json"

api_key = "YOUR_API_KEY"  # Replace with your actual API key

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(openai_api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def pdf(theme):
    # Set colors based on the selected theme
    if theme == "Dark":
        text_color = "white"
        background_color = "#0f0f0f"
        note_background = "rgba(173, 133, 71, 1)"
    else:  # Light theme
        text_color = "black"
        background_color = "white"
        note_background = "rgba(173, 133, 71, 0.1)"

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.markdown(f"<h1 style='color: {text_color};'>PDF Medical Report Analysis</h1>", unsafe_allow_html=True)

    # Sidebar instructions
    st.sidebar.markdown("<h3>Instructions</h3>", unsafe_allow_html=True)
    st.sidebar.write("1. Upload your PDF medical report.")
    st.sidebar.write("2. Click 'Process' to extract text.")
    st.sidebar.write("3. Ask questions about your report.")
    st.sidebar.write("4. Get insights from the AI chatbot.")
    
    # Highlighted note under instructions
    st.sidebar.markdown(
        f"<div style='background-color: {note_background}; padding: 10px; border-radius: 5px;'>"
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
        st.subheader(" ")
        st.markdown(f"<h3 style='color: {text_color};'>Unlock the potential of medical reports with our advanced analysis capabilities. Seamlessly engage with AI-powered chatbots trained specifically on medical content. Effortlessly extract actionable insights and gain a deeper understanding of your health data.</h3>", unsafe_allow_html=True)

        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown(f"<span style='color: {text_color};'>***Instructions for PDF Medical Report Analysis***</span>", unsafe_allow_html=True)
            st.write("1. Upload Your PDF Medical Files: Start by uploading your medical reports using the provided file uploader.")
            st.write("2. Extract Text: Once uploaded, the platform will extract text from the PDF and display it for analysis.")
            st.write("3. Interact with AI Chatbot: Engage with an AI-powered chatbot trained on the content of the PDF document. Ask questions, seek explanations, or request summaries to gain deeper insights into your medical data.")
            st.write("4. Analyze Document Content: Utilize the chatbot's responses and the extracted text to analyze the content of the medical report. Identify key points or patterns relevant to healthcare.")
            st.write("5. Extract Insights: Extract actionable medical insights from the document content and chatbot interactions. Use these insights to make informed healthcare decisions.")
            st.write("6. Iterate and Explore: Experiment with different questions and approaches to uncover hidden insights within the medical document. Refine your analysis and extract valuable knowledge.")

        # PDF uploader
        st.markdown(f"<h3 style='color: {text_color};'>Your documents</h3>", unsafe_allow_html=True)
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get PDF text
                raw_text = get_pdf_text(pdf_docs)

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Initialize conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

    with col2:
        st_lottie(l1)

    # Handle user input
    if st.session_state.conversation:
        user_question = st.text_input("Ask a question about your medical report:")
        if st.button("Submit"):
            handle_userinput(user_question)

    # Footer
    st.markdown(f"<footer style='position: fixed; bottom: 0; width: 100%; text-align: center; background-color: {background_color}; color: {text_color}; padding: 10px;'>"
                 "<p>&copy; Powered by Medicare AI ©️ 2024</p>"
                 "</footer>", unsafe_allow_html=True)

# Call the pdf function from elsewhere in your code, providing the theme
# Example: pdf("Light") or pdf("Dark")
