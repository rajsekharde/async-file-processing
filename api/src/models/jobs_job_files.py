from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum
import sqlalchemy as sa
from datetime import datetime, timezone, timedelta
from sqlalchemy.types import JSON
from dotenv import load_dotenv
import os


load_dotenv()

token_expire_days = int(os.getenv("JOB_TOKEN_EXPIRE_DAYS"))


class JobStatus(str, Enum):
    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Roles(str, Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


def now_utc():
    return datetime.now(timezone.utc)

def token_expires_at():
    return now_utc() + timedelta(days=token_expire_days)


class Job(SQLModel, table=True):

    __tablename__ = "jobs"

    job_id: UUID = Field(default_factory=uuid4, primary_key=True)

    session_id: str = Field(sa_type=sa.String)

    session_id_expires_at: datetime = Field(default_factory=token_expires_at)

    operation_type: str = Field(sa_type=sa.String)

    operation_params: dict = Field(sa_column=sa.Column(JSON))

    status: JobStatus = Field(sa_column=sa.Column(sa.String, sa.Enum(JobStatus)))

    error_message: Optional[str] = Field(default=None, sa_type=sa.String)

    created_at: datetime = Field(default_factory=now_utc)

    updated_at: datetime = Field(
        default_factory=now_utc,
        sa_column=sa.Column(sa.DateTime, default=now_utc, onupdate=now_utc)
        )
    

    job_files: list["JobFile"] = Relationship(back_populates="job")


class JobFile(SQLModel, table=True):
    
    __tablename__ = "job_files"

    file_id: UUID = Field(default_factory=uuid4, primary_key=True)

    job_id: UUID = Field(foreign_key="jobs.job_id")

    role: Roles = Field(sa_column=sa.Column(sa.String, sa.Enum(Roles)))

    filename: str = Field(sa_type=sa.String)

    storage_path: str = Field(sa_type=sa.String)

    created_at: datetime = Field(default_factory=now_utc)


    job: Job = Relationship(back_populates="job_files")