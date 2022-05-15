import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_URL = os.getenv('API_URL')


class ProdConfig(Config):
    """"""
    
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

config_options = {
    'prod':ProdConfig, 
    'dev':DevConfig
}    