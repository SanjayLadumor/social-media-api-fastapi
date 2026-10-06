from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname : str = "localhost"
    database_port : str = "enterprisedb"
    database_password : str = "son2o3ndwkkmw"
    database_name : str
    database_username : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int

    class Config:
        env_file = ".env"

settings = Settings()