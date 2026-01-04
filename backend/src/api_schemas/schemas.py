from sqlmodel import SQLModel

class JobCreate(SQLModel):
    file_path: str
    operation_params: str