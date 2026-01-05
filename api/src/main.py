from fastapi import FastAPI
from src.api_schemas.schemas import JobCreate, TestText
import uuid
import redis
from fastapi.middleware.cors import CORSMiddleware

r = redis.Redis(host="redis", port=6379, decode_responses=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.post("/test")
def test_conn(data: TestText):
    r.lpush("test", data.text)
    return {"Messsage": f"Posted: {data.text}"}