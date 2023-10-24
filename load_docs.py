from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
import streamlit as st 
import os

@st.cache_data()
def load_docs():
    documents = []
    for file in os.listdir('docs'):
        if file.endswith('.pdf'):
            pdf_path = './docs/' + file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
        elif file.endswith('.docx') or file.endswith('.doc'):
            doc_path = './docs/' + file
            loader = Docx2txtLoader(doc_path)
            documents.extend(loader.load())
        elif file.endswith('.txt'):
            text_path = './docs/' + file
            loader = TextLoader(text_path, encoding = 'utf8')
            documents.extend(loader.load())
    return documents
