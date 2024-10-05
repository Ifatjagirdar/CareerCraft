# CareerCraft: ATS-Optimized Resume Analyzer

Welcome to **CareerCraft**, an ATS-Optimized Resume Analyzer designed to help job seekers enhance their resumes and increase their chances of landing job interviews. This innovative platform leverages advanced ATS technology to analyze resumes against job descriptions, providing valuable insights and recommendations for optimization.

## Project Flow

1. **User Interaction:** The user interacts with the UI to enter the job description and upload their resume.
2. **Input Collection:** User input is collected from the UI and transmitted to the backend using the Google API key.
3. **API Call:** The input is forwarded to the Gemini Pro pre-trained model via an API call.
4. **Output Generation:** The Gemini Pro model processes the input and generates the output.
5. **Display Results:** The results are returned to the frontend for formatting and display.

To accomplish this, we need to complete the following activities:

- **Requirements Specification**
  - Create a `requirements.txt` file to list the required libraries.
  - Install the required libraries.

- **Initialization of Google API Key**
  - Generate Google API Key.
  - Initialize Google API Key.

- **Interfacing with Pre-trained Model**
  - Load the Gemini Pro pre-trained model.
  - Implement a function to get the Gemini response.
  - Implement a function to read PDF content.
  - Write a prompt for the Gemini model.

- **Model Deployment**
  - Integrate with the web framework.
  - Host the application.

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

### Detailed Breakdown of the Code

The code begins by importing necessary libraries and modules:

- **dotenv:** For loading environment variables.
- **Streamlit:** For building web applications.
- **os:** For environment variable handling.
- **PyPDF2:** For reading PDF files.
- **google.generativeai:** For accessing the Gemini model.
- **PIL:** For image handling.

The flow of the code includes the following steps:

1. **Loading Environment Variables:**
   - The code loads environment variables from a `.env` file using the `load_dotenv()` function.

2. **Google API Key Configuration:**
   - The GenerativeAI module is configured with the Google API key stored in the environment variable `GOOGLE_API_KEY`.

3. **Gemini Model Initialization:**
   - A `GenerativeModel` object named `model` is created using the Gemini Pro pre-trained model from Google, setting up the environment for generating responses.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/careercraft.git
   cd careercraft
Create a requirements.txt file:

List the required libraries:

plaintext
Copy code
streamlit
streamlit_extras
google-generativeai
python-dotenv
PyPDF2
Pillow
Install the required packages:

Open the terminal and run:

bash
Copy code
pip install -r requirements.txt
Create a .env file: (Do not hard-code your API key in the code)

bash
Copy code
touch .env
Add your Google API key to the .env file:

makefile
Copy code
GOOGLE_API_KEY=your_api_key_here
Run the application:

bash
Copy code
streamlit run app.py
Usage
Navigate to the Job Market with Confidence: Start the application to access the ATS-Optimized Resume Analyzer.
Input Job Description: Paste the job description into the provided text area.
Upload Your Resume: Upload your resume in PDF format.
Submit: Click the "Submit" button to analyze your resume against the job description.
Prior Knowledge
To complete this project, you should have prior knowledge of the following topics:

Generative AI Concepts
NLP
Generative AI
About Gemini
Gemini API
Gemini Demo
Streamlit: Streamlit Guide
FAQ
Q: How does CareerCraft analyze resumes and job descriptions?
A: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.

Q: Can CareerCraft suggest improvements for my resume?
A: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.

Q: Is CareerCraft suitable for both entry-level and experienced professionals?
A: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.

