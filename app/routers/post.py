from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from .. import models, schemas
from ..database import get_db
from ..schemas import PostModel, UpdatePost, PostResponse, CreateUser, UserResponse, PostOut
from ..oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/sqlalchemy")
def test(db:Session = Depends(get_db)):

    post = db.query(models.Post).all()
    return {"data":post}

# @router.get("/")
# async def root():
#     return {"message": "Hello World"}


# @router.get("/")
@router.get("/",response_model=List[PostOut])
def get_posts(db : Session = Depends(get_db),user_id : int = Depends(get_current_user), limit : int = 10, skip : int = 0, search : Optional[str] = ""):

    # print(limit)

    # post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # return [dict(row._mapping) for row in post]
    return post

@router.post("/",status_code = status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post : PostModel,db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):

    # cur.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # cur.execute(f"INSERT INTO posts (title,content,published) VALUES({post.title},{post.content},{post.published}) RETURNING *")
    # new_post = cur.fetchone()
    # conn.commit()

    print(current_user.email)
    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}",response_model=PostOut)
def get_post(id : int, response: Response, db: Session = Depends(get_db), current_user : int = Depends(get_current_user)):

    # cur.execute(""" SELECT * FROM posts WHERE id = %s RETURNING *""", (str(id)),)
    # post = cur.fetchone()

    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID: {id} was not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
    print(post)
        
    return post
    # return [dict(row._mapping) for row in post]

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db), current_user : int = Depends(get_current_user)):

    # cur.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """,(str(id)),)
    # idx = cur.fetchone()
    # idx = find_post_index(id)

    idx = db.query(models.Post).filter(models.Post.id == id)
    if idx.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")

    idx.delete(synchronize_session=False)
    db.commit()

    # my_posts.pop(idx)
    # conn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=PostResponse)
def update_post(id:int,post:UpdatePost,db:Session = Depends(get_db), current_user : int = Depends(get_current_user)):

    # cur.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,(post.title,post.content,post.published,str(id)),)

    post_query = db.query(models.Post).filter(models.Post.id == id)
    idx = post_query.first()
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")
 
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()