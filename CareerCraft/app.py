from dotenv import load_dotenv  # Importing dotenv to load environment variables from a .env file
import streamlit as st  # Importing Streamlit for building web applications
from streamlit_extras import add_vertical_space as avs  # Importing a Streamlit extra for layout spacing
import google.generativeai as genai  # Importing the Google Generative AI library for accessing the Gemini model
import os  # Importing the OS module for environment variable handling
import PyPDF2  # Importing PyPDF2 for reading PDF files
from PIL import Image  # Importing PIL (Python Imaging Library) for image handling

# Load environment variables from .env file
load_dotenv()  # This will read the .env file and load the environment variables

# Hard-coding the Google API key (not recommended for production)
genai.configure(api_key="AIzaSyBnmqFabYRqiQr9-c5A6ZGV6zTMpGeJcP8")  # Configuring the Generative AI model with the hard-coded API key

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')  # Creating an instance of the Gemini model for generating content

# Function to get a response from the Gemini model
def get_gemini_response(input):
    response = model.generate_content(input)  # Generating content based on the input
    return response.text  # Returning the generated text response

# Function to extract text from a PDF file
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)  # Reading the uploaded PDF file
    text = ''  # Initializing an empty string to store the extracted text
    for page_num in range(len(reader.pages)):  # Looping through each page in the PDF
        page = reader.pages[page_num]  # Getting the specific page
        text += str(page.extract_text())  # Extracting text from the page and appending it to the text variable
    return text  # Returning the combined text from all pages

# Prompt for the ATS system
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing
Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App
Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solution Architect,
Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer,
Designer, and additional specialized areas, your objective is to meticulously assess
resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial
in offering top-notch guidance for resume enhancement. Assign precise matching percentage based on the JD
(Job Description) and meticulously identify any missing keywords with utmost accuracy. 

Resume: {text}
Description: {jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all three sections.
While generating the response, put some space to separate all the three sections. 
"""

# Streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

avs.add_vertical_space(4)

col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style='text-align:justify;'>
                Introducing CareerCraft, an ATS-Optimized Resume Analyzer - your ultimate solution for optimizing
                job applications and accelerating career growth. Our innovative platform leverages advanced ATS
                technology to provide job seekers with valuable insights into their resumes' compatibility with 
                job descriptions. From resume optimization and skill enhancement to career progression guidance,
                CareerCraft empowers users to stand out in today's competitive job market. Streamline your job
                application process, enhance your skills, and navigate your career path with confidence. Join
                CareerCraft today and unlock new opportunities for professional success!
                </p>""", unsafe_allow_html=True)

with col2:
    st.image('https://cdn.dribble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)

avs.add_vertical_space(10)

col1, col2 = st.columns([3, 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Guidance')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write('Efficient Career Navigation')

with col1:
    img1 = Image.open("images/icon1.png")  # Loading the first icon image
    st.image(img1, use_column_width=True)

avs.add_vertical_space(10)

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")  # Text area for job description input
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")  # File uploader for resume

    submit = st.button("Submit")  # Submit button for analysis

    if submit:  # If the submit button is pressed
        if uploaded_file is not None:  # Check if a file is uploaded
            text = input_pdf_text(uploaded_file)  # Extract text from the uploaded PDF
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))  # Get response from Gemini model
            st.subheader(response)  # Display the response

with col2:
    img2 = Image.open("images/icon2.png")  # Loading the second icon image
    st.image(img2, use_column_width=True)

avs.add_vertical_space(10)

col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align:center;'>FAQ</h1>", unsafe_allow_html=True)  # FAQ section header
    st.write("Question: How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions,
             identifying key keywords and assessing compatibility between the two.""")
    
    avs.add_vertical_space(3)
    st.write("Question: Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume 
             for specific job openings, including suggestions for missing keywords and alignment with
             desired job roles.""")
    
    avs.add_vertical_space(3)
    st.write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering
             tailored insights and guidance to enhance their resumes and advance their careers.""")
    
with col1:
    img3 = Image.open("images/icon3.png")  # Loading the third icon image
    st.image(img3, use_column_width=True)
