from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# try:
#     Connect to your postgres DB
#     conn = psycopg2.connect(host="localhost",database="FastAPI",user="enterprisedb",password="Daryldixon#22",cursor_factory=RealDictCursor,port="5444")
#     cur = conn.cursor()
#     print("Database Connection Successfull")
# except Exception as error:
#     print("Some Error Occured")
#     print(error)

# my_posts = []
# cur.execute(""" SELECT * FROM posts """)
# data = cur.fetchall()
# for i in data:
#     my_posts.append(i)

# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post
#     return False

# def find_post_index(id):
#     for i,e in enumerate(my_posts):
#         if e["id"] == id:
#             return i

# my_posts = []
# cur.execute(""" SELECT * FROM posts """)
# data = cur.fetchall()
# for i in data:
#     my_posts.append(i)

# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post
#     return False

# def find_post_index(id):
#     for i,e in enumerate(my_posts):
#         if e["id"] == id:
#             return i