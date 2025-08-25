from fastapi import APIRouter, Depends
from crud import task as tasks_crud
from core.schemas.task import TaskOut, TaskCreate
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(
    tags=["Task"],
)


@router.get("", response_model=list[TaskOut])
async def get_tasks(
session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):

    tasks = await tasks_crud.get_all_tasks(session=session)
    return tasks



@router.post("", response_model=TaskOut)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    task_create: TaskCreate,
):
    task = await tasks_crud.create_task(
        session=session,
        task_create=task_create,
    )
    return task