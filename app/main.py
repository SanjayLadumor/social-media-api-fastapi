from fastapi import FastAPI, Depends
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/sqlalchemy")
def test(db:Session = Depends(get_db)):

    post = db.query(models.Post).all()
    return {"data":post}

@app.get("/")
async def root():
    return {"message": f"Visit : https://social-media-api-fastapi-lc2r.onrender.com/docs"}