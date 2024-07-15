# DataGPT

DataGPT is an AI-powered tool to analyze and gain insights from your CSV, XLSX, and XLS data. This application uses Google Generative AI to respond to user queries about uploaded data files.

## Features

- Upload and analyze CSV, XLSX, and XLS files.
- Interactive text input for querying the data.
- AI-generated responses to data queries.
- Modern and visually appealing UI.

## Installation

Follow these steps to set up the application:

1. **Clone the Repository**
```
   git clone https://github.com/saisruthi-kovur/DataGPT.git
   cd DataGPT
```
2. **Set Up a Virtual Environment**
```
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

## Usage
### Set up your Google Generative AI API key:
- Obtain an API key from Google Generative AI.
- Set your API key:
  - Create a .streamlit directory if it doesn't exist.
  - Create a secrets.toml file in the .streamlit directory and add your API key.
    - Configure API key
      ```
      mkdir -p .streamlit
      echo "[API]" > .streamlit/secrets.toml
      echo 'API_KEY = "your-google-generativeai-api-key"' >> .streamlit/secrets.toml
      ```

- Run the web application:
```
streamlit run app.py
```
- Access the application:
  - Open your web browser.
  - Go to `http://localhost:8501` to access the DataGPT web application.

- Upload your data file:
  - Click on the "Upload your CSV, XLSX, or XLS file" button.
  - Select the file you want to analyze.
  - The uploaded data will be displayed in a table for visualization.

- Interact with the AI model:
  - Enter your queries in the provided text area.
  - Click the "Chat with Data" button to interact with the AI model based on the uploaded data.
  - The AI model will provide insights and answers related to your queries.
 
## Reference
This application was developed using: <br/>
[Streamlit](https://streamlit.io/) <br/>
[Pandas](https://pandas.pydata.org/) <br/>
[Google Generative AI](https://ai.google.dev/) <br/>
[PandasAI](https://pandas-ai.com/)
