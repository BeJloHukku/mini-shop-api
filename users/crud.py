from users.schemas import UserScheme

def create_user(user_in: UserScheme):
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }