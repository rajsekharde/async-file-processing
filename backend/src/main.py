from fastapi import FastAPI
from src.api_schemas.schemas import JobCreate
import uuid
import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

app = FastAPI()

@app.get("/")
def root_check():
    return {"Message": "Welcome to File Processing App"}

@app.get("/health")
def health_check():
    return {"Message": "Backend is running"}

@app.post("/jobs")
def accept_job(Job: JobCreate):
    job_id = str(uuid.uuid4())
    r.lpush("jobs", job_id)
    return job_id