import os


class Config:
    SECRET_KEY = "s6d84654ae43rw5adwqe457485fd2qwd4324823"
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

