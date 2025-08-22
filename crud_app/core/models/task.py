import uuid

from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from core.enums import TaskStatus
from .base import Base


class Task(Base):
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus, name="task_status"), nullable=False, default=TaskStatus.CREATED)
