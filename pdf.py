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

api_key = "API KEYS"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    openai_api_key = api_key
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    openai_api_key = api_key
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def pdf():
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.title("PDF Medical Report Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Unlock the potential of medical reports with our advanced analysis capabilities. Seamlessly engage with AI-powered chatbots trained specifically on medical content. Effortlessly extract actionable insights and gain a deeper understanding of your health data.")
        
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for PDF Medical Report Analysis***")
            st.write("1. Upload Your PDF Medical Files: Start by uploading your medical reports using the provided file uploader.")
            st.write("2. Select Your Document: After uploading, select the medical report you wish to analyze from the dropdown menu.")
            st.write("3. Extract Text: Once selected, the platform will extract text from the PDF and display it for analysis.")
            st.write("4. Interact with AI Chatbot: Engage with an AI-powered chatbot trained on the content of the PDF document. Ask questions, seek explanations, or request summaries to gain deeper insights into your medical data.")
            st.write("5. Analyze Document Content: Utilize the chatbot's responses and the extracted text to analyze the content of the medical report. Identify key points or patterns relevant to healthcare.")
            st.write("6. Extract Insights: Extract actionable medical insights from the document content and chatbot interactions. Use these insights to make informed healthcare decisions.")
            st.write("7. Iterate and Explore: Experiment with different questions and approaches to uncover hidden insights within the medical document. Refine your analysis and extract valuable knowledge.")

    with col2:
        st_lottie(l1)
        
    user_question = st.text_input("Ask a question about your medical reports")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
