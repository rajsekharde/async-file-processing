from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_check():
    return {"Message": "Welcome to File Processing App"}

@app.get("/health")
def health_check():
    return {"Message": "Backend is running"}