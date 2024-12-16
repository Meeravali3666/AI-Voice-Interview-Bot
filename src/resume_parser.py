import fitz  # PyMuPDF

def parse_resume(pdf_path):
    """
    Extracts text from a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the resume.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return ""
