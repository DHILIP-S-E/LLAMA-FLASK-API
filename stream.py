import os
os.environ["OLLAMA_HOST"] = "http://localhost:11434"  # Must be set before importing ollama

import streamlit as st
import ollama
from PIL import Image
import base64

# Page config
st.set_page_config(
    page_title="Llama OCR",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🦙 Llama OCR")
st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Llama 3.2 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar upload
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

# Clear button top right
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.experimental_rerun()

if uploaded_file is not None:
    # Show image preview
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Extract Text 🔍"):
        with st.spinner("Processing image..."):
            try:
                image_bytes = uploaded_file.getvalue()
                img_b64 = base64.b64encode(image_bytes).decode()

                prompt = (
                    "<image>\n"
                    "Extract all text visible in the image exactly as it appears. "
                    "Provide output in clear, structured Markdown format."
                )

                response = ollama.chat(
                    model="llama3.2-vision:11b",
                    messages=[{
                        "role": "user",
                        "content": prompt,
                        "images": [img_b64]
                    }],
                )

                st.session_state['ocr_result'] = response.message.content

            except Exception as e:
                st.error(f"Error processing image: {str(e)}")

# Display OCR result
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results here.")

st.markdown("---")
st.markdown("Made with ❤️ using Llama Vision Model | [Report an Issue](https://github.com/patchy631/ai-engineering-hub/issues)")
