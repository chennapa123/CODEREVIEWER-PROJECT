import os
from dotenv import load_dotenv

# Allow local .env to override system env so we can force SQLite easily
load_dotenv(override=True)

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')

# Default to the bundled SQLite database inside the instance folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
default_sqlite_path = os.path.join(project_root, 'instance', 'app.db')
default_sqlite_uri = f"sqlite:///{default_sqlite_path}"

database_url = os.getenv('DATABASE_URL', default_sqlite_uri)

# Normalize legacy postgres scheme to SQLAlchemy 2.x recommended driver
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql+psycopg://', 1)
elif database_url.startswith('postgresql://'):
    database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)

SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_TRACK_MODIFICATIONS = False

# API Keys
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')