from fastapi import APIRouter
from ..database import databaseConnectionHandler
router = APIRouter()

@router.post("/login")
async def login(email: str, password: str):
    """
    logs in the user
    """
    return {"email": email, "password": password}

@router.post("/signup")
async def signup(email: str, password: str, name: str):
    """
    create a new user in db

    takes three strings of email, password and name
    """
    


    return {"email": email, "password": password, "name": name}


@router.post("/journal")
async def journal(data:dict[str, str, str])->dict:
    """
    create a new journal entry in db
    """

    return {"data": data}


