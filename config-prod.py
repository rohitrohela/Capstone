import os

# SECRET_KEY = os.urandom(32)
# # Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
DB_USER = os.getenv('DATABASE_URL_PRD', 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')

SQLALCHEMY_DATABASE_URI = DB_USER
SQLALCHEMY_TRACK_MODIFICATIONS = False

