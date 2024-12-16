import re

def clean_response(response):
    """
    Cleans the text response by removing unnecessary characters.

    Args:
        response (str): The response text.

    Returns:
        str: Cleaned response text.
    """
    return re.sub(r'[^\w\s]', '', response)
