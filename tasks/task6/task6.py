import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task3.task3 import DocumentProcessor
from tasks.task4.task4 import EmbeddingClient
from tasks.task5.task5 import ChromaCollectionCreator

if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-v1-423923",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        processor = DocumentProcessor()
        processor.ingest_documents()
        embed_client = EmbeddingClient(**embed_config)
        chroma_creator = ChromaCollectionCreator(processor, embed_client)

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            topic = st.text_input("Enter the quiz topic")
            num_questions = st.slider("Select the number of questions", min_value=1, max_value=20, value=5)
            document = None
            submitted = st.form_submit_button("Generate a Quiz!")
            if submitted:
                chroma_creator.create_chroma_collection()
                document = chroma_creator.query_chroma_collection(topic) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)