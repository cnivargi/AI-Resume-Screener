# ✅ Use Python as base image
FROM python:3.9

# ✅ Set working directory inside container
WORKDIR /app

# ✅ Copy all project files
COPY . .

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Expose FastAPI Port
EXPOSE 8000

# ✅ Run FastAPI with Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]