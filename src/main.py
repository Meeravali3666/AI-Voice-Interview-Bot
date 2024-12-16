import os
from resume_parser import parse_resume
from question_generator import generate_custom_question
from voice_service import speak_text, record_audio
from utils import clean_response

def main():
    pdf_path = 'Vali_Integrate.pdf'  # Replace with the path to the candidate's resume
    print("Extracting resume details...")
    resume_text = parse_resume(pdf_path)
    print(f"Parsed Resume:\n{resume_text}")

    candidate_name = "John Doe"  # Replace with name extraction logic from resume_text if needed
    print(f"Candidate Name: {candidate_name}")

    print("Starting the interview process...")
    key_info = resume_text  # Optionally refine key info using extract_key_information()
    
    question = generate_custom_question(key_info)
    print(f"First Question: {question}")
    speak_text(question)

    print("Waiting for response...")
    response = record_audio()  # Capture audio response
    if response:
        cleaned_response = clean_response(response)
        print(f"Candidate's Response: {cleaned_response}")
    else:
        print("No response captured.")

if __name__ == "__main__":
    main()
