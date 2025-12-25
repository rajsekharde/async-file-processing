from sqlmodel import SQLModel, Field
from typing import Optional
import sqlalchemy as sa
from enum import Enum
from datetime import datetime
from uuid import UUID, uuid4
from jobs import Job, now_utc


class Roles(str, Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


class JobFile(SQLModel, table=True):
    
    __tablename__ = "job_files"

    file_id: UUID = Field(default_factory=uuid4, primary_key=True)

    job_id: UUID = Field(foreign_key="jobs.job_id")

    role: Roles = Field(sa_column=sa.Column(sa.String, sa.Enum(Roles)))

    filename: str = Field(sa_type=sa.String)

    storage_path: str = Field(sa_type=sa.String)

    created_at: datetime = Field(default_factory=now_utc)