import streamlit as st
from PIL import Image
import os
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/3244e710-2470-4ade-8d4f-2654e645be11/loLAddQjXP.json"

GOOGLE_API_KEY = "API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

def object_det():
    st.title("Medical Image Analysis 🔍")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Leverage cutting-edge AI technology for medical image analysis. Our platform identifies key objects and areas in medical images, assisting in diagnostics, research, and improving overall patient care.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medical Image Analysis***")
            st.write("Upload Your Medical Image: Start by uploading an image, such as an X-ray, MRI, or other medical imagery, using the file uploader.")
            st.write("Explore Image Details: Once uploaded, the image will be displayed along with its dimensions. Review the image details before proceeding.")
            st.write("Pose Your Medical Query: Optionally, input a specific question related to the medical image, such as ‘Identify abnormalities in the lung region’.")
            st.markdown("Initiate Object Detection: Click the `Identify the objects` button to analyze the medical image. Our AI model will detect and list objects or areas of interest, providing context for further analysis.")
            st.write("View Detected Objects: The identified objects or areas of interest will be displayed on the interface. Use these insights to assist in diagnostics or medical research.")
            st.write("Iterate and Explore: Experiment with different medical images to explore the full capabilities of our image analysis tool. Iterate to refine your medical image analysis and gather valuable insights.")
            st.write("With these instructions, you're ready to utilize our Medical Image Analysis tool for accurate and insightful analysis. Let's unlock the power of AI for medical imaging!")

    with col2:
        st_lottie(l1)

    disclaimer_message = """This tool is optimized for medical images such as X-rays, MRIs, and CT scans. Upload medical images for the best results 🙂"""

    # Hide the disclaimer initially
    st.write("")

    # Show the disclaimer if the button is clicked
    with st.expander("Disclaimer ⚠️", expanded=False):
        st.markdown(disclaimer_message)
    
    # Upload medical image through Streamlit
    uploaded_image = st.file_uploader("Choose a medical image (X-ray, MRI, etc.) ...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Medical Image.", use_column_width=True)

        # Process the image (example: get image dimensions)
        image = Image.open(uploaded_image)
        width, height = image.size
        st.write("Image Dimensions:", f"{width}x{height}")

        question = st.text_input("Medical Query? (e.g., Identify abnormalities in the lung)")

        if st.button("Identify the objects"):

            st.success("Detecting...")

            vision_model = genai.GenerativeModel('gemini-1.5-pro')
            response = vision_model.generate_content([question, image])

            st.write("The objects or areas detected are: \n", response.text)

            st.success("Thanks for using the Medical Image Analysis tool! 🤩")
