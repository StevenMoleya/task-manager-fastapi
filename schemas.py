from pydantic import BaseModel
from typing import Optional

# Base schema ensuring incoming/outgoing data has correct data types


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Used when a user submits a new task


class TaskCreate(TaskBase):
    pass

# Used when sending task records back to the frontend (includes SQL ID)


class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True
