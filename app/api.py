from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import uuid
from app.resume_parser import extract_text_from_pdf
from app.db_utils import add_resume, search_resumes
from app.llm_utils import analyze_resume  # ✅ AI-powered ranking integration

app = FastAPI()

# ✅ Define the upload folder
BASE_DIR = "D:/GenAI2025/ResScr"
UPLOAD_FOLDER = os.path.join(BASE_DIR, "data/resumes")

# ✅ Ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class RankRequest(BaseModel):
    resume_text: str
    job_description: str

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    """
    API endpoint to upload a resume, extract text, store in ChromaDB, and return a unique ID.
    """
    try:
        # ✅ Generate a unique filename
        file_id = f"{file.filename.replace('.pdf', '')}_{uuid.uuid4().hex[:8]}"
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # ✅ Save file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # ✅ Extract resume text
        resume_text = extract_text_from_pdf(file_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Resume contains no extractable text.")

        # ✅ Store in ChromaDB
        add_resume(file_id, resume_text)

        return {"message": "Resume uploaded successfully", "file_id": file_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search/")
def search(request: SearchRequest):
    """
    API endpoint to search resumes based on user query.
    """
    results = search_resumes(request.query, top_k=request.top_k)
    return {"matches": results}

@app.post("/rank_resume/")
def rank_resume(request: RankRequest):
    """
    Uses LLM (DeepSeek-Coder-V2 via LM Studio) to rank a resume against a job description.
    """
    result = analyze_resume(request.resume_text, request.job_description)
    return {"analysis": result}

print("🚀 FastAPI is starting...")

if __name__ == "__main__":
    import uvicorn
    print("✅ FastAPI Server Running at http://127.0.0.1:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
