import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import timedelta

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=True

config_dict ={
    'dev': DevConfig
}