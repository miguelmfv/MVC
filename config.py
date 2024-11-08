import os
from dotenv import load_dotenv

load_dotenv()  # Carregar variáveis do .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # URI do banco de dados PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')  # Para formulários com CSRF
