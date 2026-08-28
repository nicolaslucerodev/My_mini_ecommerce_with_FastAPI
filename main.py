from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()
@app.get("/")

async def home():
    return RedirectResponse (url="/")