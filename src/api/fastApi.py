import fastapi
from pydantic_core.core_schema import DictSchema
import userRouter
app = fastapi.FastAPI()

app.include_router(userRouter.router)


@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.get("/")
async def root():
    return {"Welcome to Journey"}
