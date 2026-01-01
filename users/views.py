from fastapi import APIRouter

from users.schemas import UserScheme

from users import crud


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: UserScheme):
    return crud.create_user(user)

