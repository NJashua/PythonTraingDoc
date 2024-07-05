# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instagram.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False