import google.generativeai as genai

# Configure the Gemini AI API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_custom_question(key_info, previous_context=""):
    """
    Generates a custom interview question based on the resume information and context.

    Args:
        key_info (str): Key information from the resume.
        previous_context (str): Previous interview conversation context.

    Returns:
        str: A custom interview question.
    """
    prompt = (
        f"Generate a professional and relevant interview question based on the following resume details:\n"
        f"{key_info}\n\nPrevious context:\n{previous_context}\n"
        "Next interview question:"
    )
    try:
        response = genai.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating question: {e}")
        return "Could you tell me more about yourself?"
