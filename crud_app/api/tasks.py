from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Task"],
)


@router.get("")
def hello_world():
    return "Hello"
