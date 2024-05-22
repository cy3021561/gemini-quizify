# Gemini Quizify Mission

## Overview

The Gemini Quizify Mission is a Streamlit-based tool designed to create quizzes from PDF documents. The application processes documents, generates embeddings, and creates quiz questions based on the provided topics. Users can load PDFs, specify quiz topics, and generate multiple-choice questions. The app supports navigating through the generated questions and provides feedback on user answers.

## Features

- **Document Ingestion:** Load and process PDF documents.
- **Embedding Generation:** Generate embeddings for document content using a pre-defined model.
- **Quiz Creation:** Generate multiple-choice questions based on the document content and specified topic.
- **Interactive Quiz:** Navigate through questions, submit answers, and receive feedback.

## Requirements

- Python 3.7+
- Streamlit

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set up the embedding configuration with your model name, project ID, and location.

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run tasks/task10/task10.py
   ```

2. **Load Data:**

   - The app will prompt you to load PDF documents for ingestion.
   - Enter the topic for the quiz and specify the number of questions to generate.
   - Click the "Submit" button to start the process.

3. **Quiz Interaction:**

   - Once the questions are generated, the quiz will be displayed.
   - Navigate through questions using "Next Question" and "Previous Question" buttons.
   - Submit your answer and receive immediate feedback.
