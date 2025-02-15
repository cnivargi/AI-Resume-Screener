import requests

# ✅ LM Studio API Server
LM_STUDIO_URL = "http://localhost:1234/v1/completions"

def query_llm(prompt):
    """
    Sends a request to the LLM (DeepSeek-Coder-V2-Lite-Instruct via LM Studio).
    """
    payload = {
        "model": "deepseek-coder-v2-lite-instruct",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 500
    }
    response = requests.post(LM_STUDIO_URL, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def analyze_resume(resume_text, job_description):
    """
    Uses LLM to analyze a resume against a job description and classify the candidate.
    """
    prompt = f"""
    Analyze the following resume against this job description.
    - Extract key skills, experience, and education.
    - Classify the candidate into:
      * 'Good Fit'
      * 'Needs Review'
      * 'Not a Fit'
    - Provide a brief explanation of the ranking.

    **Job Description:**
    {job_description}

    **Resume Content:**
    {resume_text}
    """
    return query_llm(prompt)

# ✅ Test the LLM Connection
if __name__ == "__main__":
    sample_resume = "Nivargi"
    sample_job = "SAP"
    
    response = analyze_resume(sample_resume, sample_job)
    print(response)
