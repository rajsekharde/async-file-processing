from fastapi import FastAPI, File, UploadFile, HTTPException
from src.api_schemas.schemas import JobCreate, TestText
import uuid
import redis
import shutil
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

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


BASE_DIR = Path("/data")
UPLOADS = BASE_DIR / "uploads"
RESULTS = BASE_DIR / "results"


@app.post("/upload")
async def upload_files(file : UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No Filename")
    
    job_id = str(uuid.uuid4())
    job_upload_dir = UPLOADS / job_id
    job_upload_dir.mkdir(parents=True, exist_ok=True)

    safe_name = f"{uuid.uuid4()}_{Path(file.filename).name}"
    dest = job_upload_dir / safe_name

    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    
    r.lpush("jobs", job_id)

    return {
        "Job Id": job_id,
        "File Name": safe_name
    }

