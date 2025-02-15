import os
import pdfplumber

# Set up correct base directory
BASE_DIR = "D:/GenAI2025/ResScr"  # Base project folder
RESUME_DIR = os.path.join(BASE_DIR, "data/resumes")  # Resumes folder

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def process_all_resumes():
    """
    Reads all PDFs in the resumes folder and extracts text.
    """
    if not os.path.exists(RESUME_DIR):
        print(f"Error: Directory '{RESUME_DIR}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(RESUME_DIR) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the resumes directory.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(RESUME_DIR, pdf_file)
        print(f"\nExtracting text from: {pdf_file}")
        extracted_text = extract_text_from_pdf(pdf_path)
        print(extracted_text[:500])  # Print first 500 characters for preview

# Run the script
if __name__ == "__main__":
    process_all_resumes()