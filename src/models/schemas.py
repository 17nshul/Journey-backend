from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr  # Validates email format automatically
    name: str  # Changed from full_name to match your model

class UserCreate(UserBase):
    password: str  # Only for creation requests

class UserResponse(UserBase):
    created_at: datetime
    # Never return password hashes in responses!

    class Config:
        from_attributes = True  # Enables ORM model -> schema conversion

class JournalEntryBase(BaseModel):
    entry_text: str
    mood: Optional[str] = None

class JournalEntryCreate(JournalEntryBase):
    user_email: EmailStr

class JournalEntryResponse(JournalEntryBase):
    id: int
    created_at: datetime
    user_email: EmailStr

    class Config:
        from_attributes = True