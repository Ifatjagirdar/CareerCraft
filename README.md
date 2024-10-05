# CareerCraft: ATS-Optimized Resume Analyzer

Welcome to **CareerCraft**, an ATS-Optimized Resume Analyzer designed to help job seekers enhance their resumes and increase their chances of landing job interviews. This innovative platform leverages advanced ATS technology to analyze resumes against job descriptions, providing valuable insights and recommendations for optimization.

## Features

- **ATS-Optimized Resume Analysis:** Assess your resume's compatibility with job descriptions.
- **Resume Optimization:** Get personalized suggestions for improving your resume.
- **Skill Enhancement:** Identify skills you should highlight or acquire for specific roles.
- **Career Progression Guidance:** Receive insights to help you navigate your career path.
- **Streamlined Application Process:** Simplify the process of applying for jobs.
- **Personalized Recommendations:** Tailored advice based on your unique qualifications and goals.
- **Efficient Career Navigation:** Tools to help you move forward in your career confidently.

## Technologies Used

- **Streamlit:** For building the web application interface.
- **Google Generative AI (Gemini):** To generate content and analyze resumes.
- **PyPDF2:** For reading PDF files (resumes).
- **Pillow (PIL):** For image handling.
- **dotenv:** For managing environment variables.

## Code Overview

The codebase consists of the following key components:

1. **Environment Setup:**
   - Utilizes `dotenv` to load environment variables from a `.env` file, ensuring sensitive information like API keys are not hard-coded into the application.

2. **Streamlit Interface:**
   - The user interface is built using Streamlit, featuring sections for job description input, resume upload, and displaying analysis results.

3. **Gemini Model Integration:**
   - Integrates with the Google Generative AI (Gemini) model to generate insights based on the user's resume and the job description.

4. **PDF Text Extraction:**
   - Uses `PyPDF2` to extract text from uploaded PDF resumes, making the content accessible for analysis.

5. **Response Generation:**
   - The application generates a response that includes a matching percentage with the job description, lists missing keywords, and provides a summary of the candidate's profile.

