from pydantic import BaseModel
from pydantic import ConfigDict
from uuid import UUID

from core.enums import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None


class TaskOut(TaskBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: UUID
    status: TaskStatus
