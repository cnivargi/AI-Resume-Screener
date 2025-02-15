import os
import pdfplumber
import uuid
from app.db_utils import add_resume  # Ensure correct import

# Define correct resume folder
BASE_DIR = "D:/GenAI2025/ResScr"
RESUME_DIR = os.path.join(BASE_DIR, "data/resumes")

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
    Reads all PDFs in the resumes folder, extracts text, and stores them in ChromaDB.
    """
    if not os.path.exists(RESUME_DIR):
        print(f"❌ Error: Directory '{RESUME_DIR}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(RESUME_DIR) if f.endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the resumes directory.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(RESUME_DIR, pdf_file)
        extracted_text = extract_text_from_pdf(pdf_path)

        if not extracted_text.strip():  # Check if resume text is empty
            print(f"⚠️ Warning: {pdf_file} contains no extractable text. Skipping...")
            continue

        # Generate a unique ID for each resume
        file_id = pdf_file.replace(".pdf", "") + "_" + str(uuid.uuid4())[:8]

        # Store in ChromaDB
        add_resume(file_id, extracted_text)

        print(f"✅ Stored {pdf_file} in ChromaDB with ID: {file_id}")

# Run the script
if __name__ == "__main__":
    process_all_resumes()
