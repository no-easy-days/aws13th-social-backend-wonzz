import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


# 회원가입 기능
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="사용자 이름")
    age: int = Field(..., ge=0, le=100, description="나이 (0~100)")
    email: EmailStr
    nickname: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

# 로그인 기능
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    pass

class UserResponse(BaseModel):
    pass

























