from pydantic import BaseModel, EmailStr, Field

class UserScheme(BaseModel):
    username: str = Field(..., min_length=2, max_length=20)
    email: EmailStr