import PyPDF2
import io

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.
    Args:
        pdf_file: Streamlit uploaded file object
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def is_valid_pdf(file):
    """
    Check if the uploaded file is a valid PDF.
    Args:
        file: Streamlit uploaded file object
    Returns:
        bool: True if valid PDF, False otherwise
    """
    return file.type == "application/pdf" 