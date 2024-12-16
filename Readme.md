
# **AI VOICE Interview Bot**

### **Automating Interviews with AI for Efficiency and Fairness**

---

## **Overview**
The **AI Interview Bot** is a Python-based project that automates the interview process. It leverages advanced AI technologies to parse resumes, generate context-specific interview questions, and interact with candidates via voice. This bot streamlines HR workflows, providing unbiased evaluations and detailed insights.

---

### **Key Features**
- **Resume Parsing**:
  - Extracts structured information from PDF resumes using PyMuPDF.
- **AI-Generated Questions**:
  - Uses the Gemini API to create personalized interview questions tailored to each candidate's resume.
- **Voice Interaction**:
  - Converts questions to audio using Pyttsx3 and processes responses via SpeechRecognition.
- **Insight Generation**:
  - Summarizes the interview conversation and provides feedback for HR teams.
- **Error Handling**:
  - Robust handling of audio processing errors and unexpected inputs.

---

### **Technologies Used**
| **Technology**           | **Purpose**                               |
|---------------------------|-------------------------------------------|
| **PyMuPDF**               | Extracts text from resumes (PDF parsing). |
| **Gemini API**            | Generates questions and insights.         |
| **Pyttsx3**               | Converts text to speech.                 |
| **SpeechRecognition**     | Converts speech to text.                 |
| **Python**                | Core programming language.               |

---

## **System Architecture**

1. **Frontend**:
   - Candidates interact with the system via a web or desktop interface to upload resumes and answer interview questions.
2. **Backend**:
   - Processes resumes, generates questions, manages voice services, and stores insights.
3. **Services**:
   - AI tools for parsing resumes, generating questions, and converting text/speech.
4. **Storage**:
   - Stores resumes, transcripts, and insights for future reference.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/AI-Interview-Bot.git
cd AI-Interview-Bot
```

### **2. Set Up Virtual Environment**
Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **4. Configure the Gemini API**
Replace `YOUR_GEMINI_API_KEY` in the code with your actual Gemini API key. You can set it as an environment variable for security:
```bash
export GEMINI_API_KEY=your_actual_api_key
```

---

## **Usage**

1. **Run the Application**:
   ```bash
   python src/main.py
   ```

2. **Upload Resume**:
   - Replace `Vali_Integrate.pdf` in the `main.py` file with the path to the resume file.

3. **Answer Questions**:
   - The bot will ask questions based on the resume.
   - Respond via microphone, and the bot will process your answers.

4. **Review Logs**:
   - Interview transcripts and insights are saved in the `interview_logs/` directory.

---

## **Folder Structure**
```
AI-Interview-Bot/
│
├── .gitignore                # Files to be ignored by Git
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── src/                      # Source code directory
│   ├── __init__.py           # Marks the folder as a Python package
│   ├── main.py               # Entry point of the application
│   ├── resume_parser.py      # Resume parsing functionality
│   ├── question_generator.py # Question generation logic
│   ├── voice_service.py      # Voice interaction services
│   └── utils.py              # Helper functions
│
└── interview_logs/           # Stores interview transcripts and insights
```

---

## **Examples**

### **Sample Input**:
- Resume: `Resume.pdf`
- Key Details Extracted:
  - **Name**: John Doe
  - **Skills**: Python, Data Science, Machine Learning
  - **Education**: Bachelor's in Computer Science
  - **Experience**: 3 years at XYZ Company

### **Sample Interaction**:
1. **Bot**: "Hello John Doe! Can you tell me about your experience at XYZ Company?"
2. **Candidate**: [Responds via microphone].
3. **Bot**: "Great! How do you apply Python in your current role?"

### **Sample Output**:
- **Transcript**:
  ```
  Q1: Tell me about your experience at XYZ Company.
  A1: I led a data science team to build predictive models for customer segmentation.
  ```
- **Insights**:
  - Strong skills in Python and machine learning.
  - Leadership experience in data science.

---

## **Challenges & Solutions**
| **Challenge**               | **Solution**                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| Poor audio quality           | Implemented retries and error-handling for audio recognition failures.       |
| Generating relevant questions| Used Gemini API to ensure context-aware, personalized questions.             |
| Large resume datasets        | Optimized text extraction and storage handling.                              |
| Graceful interview termination| Added functionality to save progress if the candidate stops mid-interview.  |

---

## **Future Scope**
- **Multilingual Support**: Handle interviews in multiple languages.
- **Video Interviewing**: Add real-time video-based interaction with facial analysis.
- **Advanced Analytics**: Build dashboards for HR to analyze trends and compare candidates.

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes and push:
   ```bash
   git push origin feature/new-feature
   ```
4. Open a pull request.



---

