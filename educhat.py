import streamlit as st
import google.generativeai as genai
import os
import shutil
import cv2
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import textwrap
import numpy as np

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Sidebar
# option = st.sidebar.selectbox(
#     'Which task do you want to perform?',
#     ('Audio', 'Video', 'Wiki'))
option = st.sidebar.radio(
    'Which task do you want to perform?',
    ('Audio', 'Video', 'Wiki'))

# Audio
if option == 'Audio':
    uploaded_file = st.file_uploader("Choose an audio file")
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        audio_file = genai.upload_file(path=uploaded_file)
        prompt = "Listen carefully to the following audio file. Provide a brief summary."
        response = model.generate_content([prompt, audio_file])
        st.write(response.text)

# Video
elif option == 'Video':
    uploaded_file = st.file_uploader("Choose a video file")
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        # Add your video processing code here

# Wiki
elif option == 'Wiki':
    search_query = st.text_input("Enter your search query")
    # if search_query:
        # Add your wiki processing code here