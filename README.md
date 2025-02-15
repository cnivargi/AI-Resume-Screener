# 🚀 AI-Powered Resume Screening System

## 📌 Overview
This **AI-powered Resume Screener** helps **HR teams** process resumes **faster and smarter** using **AI and semantic search**.  
The system **extracts key details**, **matches resumes to job descriptions**, and **ranks candidates automatically**.

## ✅ Features
- 🔍 **AI-Based Resume Analysis** (Extracts skills, experience, education)  
- 📊 **Automated Candidate Ranking** (Ranks based on job description match)  
- ⚡ **Fast & Scalable** (Uses **FastAPI + ChromaDB** for rapid search)  
- 🏗 **Customizable** (Supports **local LLMs via LM Studio** or **OpenAI API**)  
- ☁ **Deployable** (Can run **locally or on the cloud**)  

## 🛠 Technology Stack
| **Component**   | **Technology Used** |
|---------------|------------------|
| **Backend API** | FastAPI |
| **AI Processing** | DeepSeek, Llama, or OpenAI |
| **Database** | ChromaDB (for semantic search) |
| **Resume Parsing** | PyMuPDF, pdfplumber |
| **Containerization** | Docker |
| **Cloud Deployment** | AWS / Azure / GCP |

---

## 🏗 How It Works
### **🔹 Step 1: HR Uploads a Resume**
- Users can **upload resumes** via API  
- The system **extracts text** from PDFs

### **🔹 Step 2: Resume is Processed**
- AI extracts **name, skills, experience, and education**  
- ChromaDB stores resume **embeddings for fast retrieval**

### **🔹 Step 3: AI Matches Resumes to Job Description**
- Users enter a **job description**  
- AI ranks candidates based on **skill match & experience**  
- HR sees **top-ranked candidates**

---

## 📷 **AI Resume Screener Workflow**
![AI Resume Screener Workflow](https://via.placeholder.com/800x400?text=Flowchart+Image)  -- This is coming soon

**Flowchart Steps:**  
1️⃣ **Resume Upload** → 2️⃣ **Text Extraction** → 3️⃣ **Semantic Embedding (ChromaDB)** → 4️⃣ **AI Matching** → 5️⃣ **Ranking Candidates**  

📩 Contact

👨‍💻 Created by: [Chittaranjan G Nivargi]

📧 Contact: c.nivargi@gmail.com

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screener.git
cd AI-Resume-Screener
