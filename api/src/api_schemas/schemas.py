from sqlmodel import SQLModel

class JobCreate(SQLModel):
    file_path: str
    operation_params: str

class TestText(SQLModel):
    text: str