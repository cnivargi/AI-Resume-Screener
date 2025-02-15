import chromadb
from sentence_transformers import SentenceTransformer
import os

# Define Database Path
BASE_DIR = "D:/GenAI2025/ResScr"
DB_PATH = os.path.join(BASE_DIR, "data/chroma_db")  # ChromaDB storage directory

# Load embedding model (efficient for resume search)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB (Persistent Mode)
chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="resumes")

def add_resume(file_id, resume_text):
    """
    Stores the resume text as an embedding in ChromaDB.
    """
    embedding = embedding_model.encode(resume_text).tolist()
    collection.add(ids=[file_id], embeddings=[embedding], metadatas=[{"text": resume_text}])
    print(f"✅ Added resume {file_id} to ChromaDB")

def search_resumes(query, top_k=3, similarity_threshold=2.0):  # ✅ Increased from 0.7 to 2.0
    """
    Searches resumes based on job description or keyword using semantic search.
    Filters out results below the similarity threshold.
    """
    query_embedding = embedding_model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)

    if not results["ids"]:
        print("❌ No relevant resumes found.")
        return []

    filtered_results = []
    print("\n🔍 Top Matching Resumes:")

    for i, file_id in enumerate(results["ids"][0]):
        score = results["distances"][0][i]  # Lower score = better match

        if score > similarity_threshold:  # ✅ Ignore only very weak matches
            print(f"⚠️ Ignored {file_id} (Weak Match, Score: {round(score, 4)})")
            continue

        print(f"⭐ Rank {i+1}: {file_id} (Similarity Score: {round(score, 4)})")
        print(f"📄 Resume Excerpt: {results['metadatas'][0][i]['text'][:300]}...\n")

        filtered_results.append({
            "rank": i+1,
            "file_id": file_id,
            "score": round(score, 4),
            "excerpt": results['metadatas'][0][i]['text'][:300]
        })

    if not filtered_results:
        print("❌ No resumes passed the similarity threshold.")
    
    return filtered_results

# ✅ Standalone mode: Allows searching from terminal
if __name__ == "__main__":
    print("🔍 Testing ChromaDB connection...")

    user_query = input("Enter a job title, company, or skill to search resumes: ")
    print(f"🔎 Searching for: {user_query}")  # ✅ Debug print

    results = search_resumes(user_query, top_k=3)

    if not results:
        print("❌ No results found. Try a different query.")
