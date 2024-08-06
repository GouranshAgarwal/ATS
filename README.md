# ATS (Applicant Tracking System) 💻

Welcome to the Simple ATS project! This straightforward Applicant Tracking System, built with Streamlit, helps you get familiar with Large Language Models (LLMs). It offers basic functionalities to manage job applications and candidate information by analyzing resumes against job descriptions.


## 🌟 Features

- **Resume Analysis**: Upload a resume in PDF format and get an analysis of its match with a given job description.
- **Keyword Insights**: Identify missing keywords in the resume based on the job description.
- **Profile Summary**: Get a concise summary of the candidate's profile.
- **User-Friendly Interface**: Easy-to-use interface with clear sections for job description, resume upload, and results.

## 🚀 Installation

To get started with the Simple ATS, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/GouranshAgarwal/ATS.git
    cd ats
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**:
    - Create a `.env` file in the project directory.
    - Add your Gemini API key to the `.env` file:
      ```env
      GEMINI_API_KEY=your_api_key_here
      ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run ATS.py
    ```

## 📝 Usage

Once the app is running, you can access it in your web browser at `http://localhost:8501`. Follow these steps to use the ATS:

1. **Enter Job Description**: Provide a detailed job description in the text area.
2. **Upload Resume**: Upload the candidate's resume in PDF format.
3. **Submit**: Click the "Submit" button to get the analysis.



