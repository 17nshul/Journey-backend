from fastapi import APIRouter
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
    """

    return {"email": email, "password": password, "name": name}