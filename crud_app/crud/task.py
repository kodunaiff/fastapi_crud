from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Task
from core.schemas.task import TaskCreate


async def get_all_tasks(session: AsyncSession) -> Sequence[Task]:
    stmt = select(Task).order_by(Task.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_task(
    session: AsyncSession,
    task_create: TaskCreate,
) -> Task:
    task = Task(**task_create.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task