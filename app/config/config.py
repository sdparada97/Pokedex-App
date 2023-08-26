import os
from pathlib import Path
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR.parent.joinpath('.env.example')

load_dotenv(ENV_FILE)

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

config_dict ={
    'dev': DevConfig
}