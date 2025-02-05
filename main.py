# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FLH-7R4iGlU6Sa_HF37MSabHQ2rK5jqv
"""

import os
import sys
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from doc_chat_utils import get_answer

st.set_page_config(
    page_title="Chat with document",
    page_icon="👋",
    layout = "centered"
)

st.title("Document- Q/A session")

uploader_file = st.file_uploader(label = "Upload your file", type=["pdf"])

user_query  = st.text_input(label = "Enter your question.")

if st.button("Run"):
  bytes_data = uploader_file.read()
  file_name = uploader_file.name

  file_path = os.path.join(working_dir, file_name)
  with open(file_path, "wb") as f:
    f.write(byes_data)

  answer = get_answer(file_name, user_query)
  st.success(answer)
