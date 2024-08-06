import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Streamlit page configuration
st.set_page_config(
    page_title="Application Tracking System 💻",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Prompt Template
input_prompt = """
You are a skilled and very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering,
data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive and you should provide the best assistance for improving the resumes. 
Assign the percentage matching based on the job description and the missing keywords with high accuracy.
Resume:
Description:

I want the only response in 3 sections as follows:
* Job Description Match: 
* Missing Keywords: 
* Profile Summary: 
"""

# Streamlit App
st.header("📑 APPLICATION TRACKING SYSTEM 🤖")
st.markdown("### Improve Your Resume ATS Score")
st.markdown(
    """
    Welcome to the Application Tracking System. Upload your resume and provide a job description to get an analysis of your resume's match with the job description. 
    Get insights on missing keywords and a summary of your profile.
    """
)

# Input fields
st.subheader("Job Description 📝")
jd = st.text_area("Enter the Job Description here...")

st.subheader("Upload Your Resume")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", help="Please upload your resume in PDF format.")

# Button to submit
submit = st.button("Submit 🚀")

# Process the input when submit button is clicked
if submit:
    if uploaded_file is not None and jd:
        # Extract text from the uploaded PDF resume
        reader = pdf.PdfReader(uploaded_file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()

        # Combine the job description and resume into the prompt
        prompt = f"{input_prompt} Resume: {extracted_text} Description: {jd}"
        
        # Generate content using the generative model
        response = model.generate_content(prompt)
        
        # Debug output to understand the response format
        st.markdown("## Debug: Response Content")
        st.write(response.text)
        
        # Check if the response contains the expected sections
        response_text = response.text
        if "* Job Description Match:" in response_text and "• Missing Keywords:" in response_text and "* Profile Summary:" in response_text:
            job_match = response_text.split("* Job Description Match:")[1].split("• Missing Keywords:")[0]
            missing_keywords = response_text.split("• Missing Keywords:")[1].split("* Profile Summary:")[0]
            profile_summary = response_text.split("* Profile Summary:")[1]
            
            st.markdown("## Results")
            st.markdown("### Job Description Match")
            st.write(job_match)
            
            st.markdown("### Missing Keywords")
            st.write(missing_keywords)
            
            st.markdown("### Profile Summary")
            st.write(profile_summary)
        else:
            st.error("The response format is not as expected. Please try again.")
    elif not jd:
        st.error("Please enter the Job Description.")
    else:
        st.error("Please upload your resume.")

# Enhanced Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    """
    This Application Tracking System (ATS) helps you improve your resume by matching it against job descriptions.
    It provides insights into missing keywords and gives a profile summary to help you stand out in a competitive job market.
    """
)

st.sidebar.subheader("Tips for Using the ATS")
st.sidebar.markdown(
    """
    - Ensure your resume is in PDF format.
    - Provide a detailed job description for better analysis.
    - Use clear and concise language in your resume.
    - Highlight your skills and experience that match the job description.
    """
)

st.sidebar.subheader("Navigation")
st.sidebar.markdown(
    """
    - [Home](#)
    - [Upload Resume](#upload-your-resume)
    - [Job Description](#job-description)
    - [Results](#results)
    """
)

st.sidebar.subheader("Contact")
st.sidebar.markdown("https://www.linkedin.com/in/gouransh-agarwal-907281288/](https://www.linkedin.com) | [https://github.com/GouranshAgarwal](https://github.com)")
st.sidebar.markdown(
    """
    For any issues or suggestions, please contact us at [your-email@example.com](mailto:your-email@example.com).
    """
)