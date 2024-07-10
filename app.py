# Import necessary libraries and modules
import streamlit as st
import pandas as pd
from pandasai import PandasAI
import os
import google.generativeai as genai

# Configure Google Generative AI
API_KEY = st.secrets["API"]["API_KEY"]
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom wrapper class for Generative AI to make it compatible with PandasAI
class CustomGenAILLM:
    def __init__(self, model):
        self.model = model
        self._llm_type = "genai"

    def __call__(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while processing your request."

    @property
    def type(self):
        return self._llm_type

# Set page configuration and title for Streamlit
st.set_page_config(page_title="DataGPT", page_icon="📊", layout="wide")

# Custom CSS for a better UI
custom_css = """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #1f77b4;
        color: white;
        padding: 10px 24px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #104e8b;
    }
    .stTextInput>div>div>textarea, .result-container {
        border-radius: 4px;
        padding: 10px;
        background-color: #ffffff;
        color: #333333;
        border: 2px solid #e1e5eb;
    }
    .stTextInput>div>div>textarea::placeholder {
        color: #888888; /* Placeholder text color */
    }
    .stTextInput>div>div>textarea:focus, .result-container:focus {
        border-color: #1f77b4;
    }
    .stDataFrame {
        border: 2px solid #1f77b4;
        border-radius: 4px;
    }
    .stMarkdown p {
        font-size: 18px;
        color: #333333;
    }
    .stMarkdown h1 {
        color: #1f77b4;
    }
    .result-container strong {
        color: #333333; /* Ensuring text color is visible */
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Add header with title and description
st.markdown(
    '<h1 style="text-align:center;">📊 DataGPT</h1>'
    '<p style="text-align:center;">An AI-powered tool to analyze and gain insights from your CSV, XLSX, and XLS data.</p>',
    unsafe_allow_html=True
)

def chat_with_csv(df, prompt):
    llm = CustomGenAILLM(model)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    return result

input_file = st.file_uploader("Upload your CSV, XLSX, or XLS file", type=['csv', 'xlsx', 'xls'], accept_multiple_files=False)

if input_file is not None:
    st.info("File Uploaded Successfully")
    if input_file.name.endswith('.csv'):
        data = pd.read_csv(input_file)
    else:
        data = pd.read_excel(input_file)
    
    st.dataframe(data, use_container_width=True)

    input_text = st.text_area("Enter your query below", placeholder="e.g., Show me the summary statistics of the data")

    if st.button("Chat with Data"):
        if input_text:
            with st.spinner("Processing..."):
                result = chat_with_csv(data, input_text)
                st.info("Your Query: " + input_text)
                st.markdown(f"<div class='result-container'><strong>Result:</strong> {result}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a query to chat with the file data.")

# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
