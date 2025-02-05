# -*- coding: utf-8 -*-
"""doc_chat_utils.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aj2HJXREK53Q6hk47OaUafLC_lZqi1Bl
"""

import os

from langchain_community.llms import Ollama
from langchain.document_loaders import UnstructuredFileLoader
from langchain_unstructured import UnstructuredLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

working_dir = os.path.dirname(os.path.abspath(__file__))

llm = Ollama(
    model="llama3: instruct",
    temperature=0
)

embeddings = HuggingFaceEmbeddings()

def get_answer(file_name, query):
  file_path = f"{working_dir}/{file_name}"

  #loading document
  loader = UnstructuredLoader(file_path)
  documents= loader.load()

  #creating text chunks
  text_splitter = CharacterTextSplitter(seperator="/n",
                                        chunk_size = 1000,
                                        chunk_overlap =200
                                        )
  text_chunks = text_splitter.split_documents(documents)

  #creating vector store
  knowledge_base = FAISS.from_documents(text_chunks, embeddings)

  qa_chain = RetrievalQA.from_chain_type(
      llm=llm,
      chain_type="stuff",
      retriever= knowledge_base.as_retriever()
  )

  response = qa_chain.invoke({"query": query})

  return response["result"]
