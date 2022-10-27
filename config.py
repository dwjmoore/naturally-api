from dotenv import load_dotenv
import os

load_dotenv

class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]

    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE= 'None'