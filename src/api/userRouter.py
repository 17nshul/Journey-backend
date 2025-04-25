from fastapi import APIRouter,Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.databaseConnectionHandler import get_db
from ..models import schemas, dbModels
from passlib.context import CryptContext
from datetime import datetime

from ..models.dbModels import JournalEntry
from ..models.schemas import JournalEntryCreate

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: schemas.UserCreate,db: Session = Depends(get_db())):
    """
    create a new user in db

    takes three strings of email, password and name
    """
    try:
        # Check for existing user
        existing_user = db.query(dbModels.User).filter(dbModels.User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash the password
        hashed_password = pwd_context.hash(user_data.password)

        # Create new user instance
        new_user = dbModels.User(
            email=str(user_data.email),
            password=hashed_password,
            name=user_data.name,
            created_at=datetime.now()
        )

        # Insert into database
        db.add(new_user)
        db.commit()  # Persist the data
        db.refresh(new_user)  # Refresh to get auto-generated fields

        # Return the user data (excluding password)
        return new_user  # Automatically converted to UserResponse
    except Exception as e:
        db.rollback()  # Rollback on error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )


@router.post("/login")
async def login(email: str, password: str, db: Session = Depends(get_db)):
    """
    login the user
    """
    user = db.query(dbModels.User).filter(dbModels.User.email == email).first()

    # Verify user exists and password matches
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # jwt tokens
    access_token = "generated_jwt_token_here"

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_email": user.email
    }

@router.post("/journal")
async def journal(entry_data: JournalEntryCreate, db: Session = Depends(get_db)):
    """
    create a new journal entry in db
    """
    try:
        # Verify user exists
        user = db.query(dbModels.User).filter(dbModels.User.email == entry_data.user_email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Create new journal entry
        new_entry = JournalEntry(
            user_email=str(entry_data.user_email),
            entry_text=entry_data.entry_text,
            mood=entry_data.mood,
            created_at=datetime.now()
        )

        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return new_entry

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create journal entry: {str(e)}"
        )